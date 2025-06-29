import os
from datetime import timedelta

class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your-jwt-secret-key-here'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)  # token有效期30天
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/avatars')
    RECIPES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/recipes')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 限制上传文件大小为5MB
    
    # 微信小程序配置
    WECHAT_APPID = os.environ.get('WECHAT_APPID') or 'your-wechat-appid-here'
    WECHAT_SECRET = os.environ.get('WECHAT_SECRET') or 'your-wechat-secret-here'
    
    # Excel数据库路径
    EXCEL_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/database.xlsx')
    
    # 豆包视觉模型API配置
    DOUBAO_API_KEY = os.environ.get('DOUBAO_API_KEY') or 'your-doubao-api-key-here'
    DOUBAO_API_URL = 'https://ark.cn-beijing.volces.com/api/v3/chat/completions'
    DOUBAO_MODEL = 'doubao-1-5-vision-pro-32k-250115'
    
    # 确保目录存在
    @staticmethod
    def init_app(app):
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(Config.RECIPES_FOLDER, exist_ok=True)
        os.makedirs(os.path.dirname(Config.EXCEL_DB_PATH), exist_ok=True)

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 