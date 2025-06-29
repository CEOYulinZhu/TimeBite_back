# 食光机小程序后端

一个基于Flask的智能食材管理与菜谱推荐系统，通过AI图像识别技术帮助用户管理食材库存，减少食物浪费，提供个性化菜谱推荐。

## 🌟 核心功能

### 用户管理系统
- **微信小程序登录**：基于微信授权的用户认证系统
- **用户信息管理**：昵称、头像、健康目标等个人信息维护
- **JWT身份验证**：安全的token认证机制，支持30天免登录
- **头像上传存储**：支持用户自定义头像上传与管理

### 智能食材管理
- **食材库存管理**：添加、更新、删除食材库存信息
- **过期日期追踪**：实时监控食材保质期，智能提醒
- **食材分类统计**：按类别统计食材数量，可视化展示
- **临期食材预警**：自动识别即将过期食材，减少浪费
- **批量操作支持**：支持批量添加和管理食材

### AI图像识别
- **食物智能识别**：基于豆包AI视觉模型的食物图像识别
- **多食材检测**：单张图片可识别多种食材及其数量
- **置信度评估**：为每种识别结果提供可信度评分
- **营养信息提取**：自动获取食材营养价值和保存建议
- **趣味知识推送**：为识别的食材提供有趣的科普知识

### 智能菜谱推荐
- **个性化推荐**：基于用户食材库存的精准菜谱匹配
- **临期食材优先**：优先推荐使用即将过期食材的菜谱
- **匹配度计算**：智能计算菜谱与用户食材的匹配程度
- **多维度筛选**：支持按烹饪时间、难度、卡路里等筛选
- **详细制作指南**：提供完整的烹饪步骤和用料清单

### 数据统计分析
- **食材库存概览**：新鲜、临期、过期食材数量统计
- **使用趋势分析**：食材消耗模式和习惯分析
- **浪费率统计**：帮助用户了解食物浪费情况
- **健康指标追踪**：营养摄入和健康目标达成情况

## 🛠 技术栈

### 后端架构
- **开发语言**：Python 3.8+
- **Web框架**：Flask 2.2.3
- **身份认证**：Flask-JWT-Extended 4.4.4
- **数据处理**：pandas 1.5.3
- **图像处理**：Pillow 10.0.0

### 数据存储
- **数据库**：Excel数据库（基于pandas + openpyxl）
- **文件存储**：本地文件系统（头像、菜谱图片）
- **数据格式**：结构化Excel表格，支持多Sheet管理

### AI集成
- **视觉识别**：豆包AI视觉模型API
- **模型版本**：doubao-1-5-vision-pro-32k-250115
- **识别能力**：多食材检测、数量估算、营养分析

### 部署运维
- **WSGI服务器**：Gunicorn 20.1.0
- **开发调试**：Flask内置开发服务器
- **环境管理**：python-dotenv支持环境变量配置

## 📁 项目结构

```
食光机-后端/
├── app.py                      # 应用入口文件
├── config.py                   # 应用配置管理
├── extensions.py               # Flask扩展初始化
├── requirements.txt            # 项目依赖清单
│
├── controllers/                # 控制器层 - 处理HTTP请求
│   ├── food_vision_controller.py      # 食物图像识别控制器
│   ├── ingredient_controller.py       # 食材管理控制器
│   ├── recipe_controller.py           # 菜谱管理控制器
│   ├── recipe_detail_controller.py    # 菜谱详情控制器
│   ├── recipe_matching_controller.py  # 菜谱匹配控制器
│   ├── recommendation_controller.py   # 推荐系统控制器
│   └── user_controller.py             # 用户管理控制器
│
├── models/                     # 数据模型层
│   ├── __init__.py
│   ├── recipe.py              # 菜谱数据模型
│   └── user.py                # 用户数据模型
│
├── repositories/               # 数据访问层
│   ├── recipe_repository.py   # 菜谱数据访问
│   └── user_repository.py     # 用户数据访问
│
├── routes/                     # 路由定义层
│   ├── __init__.py            # 路由注册中心
│   ├── food_vision.py         # 图像识别路由
│   ├── ingredient.py          # 食材管理路由
│   ├── recipe.py              # 菜谱相关路由
│   ├── recommendation.py      # 推荐系统路由
│   └── user.py                # 用户管理路由
│
├── services/                   # 业务逻辑层
│   ├── food_vision_service.py         # 食物识别业务逻辑
│   ├── ingredient_service.py          # 食材管理业务逻辑
│   ├── recipe_service.py              # 菜谱管理业务逻辑
│   ├── recipe_detail_service.py       # 菜谱详情业务逻辑
│   ├── recipe_matching_service.py     # 菜谱匹配业务逻辑
│   ├── recommendation_service.py      # 推荐算法业务逻辑
│   └── user_service.py               # 用户管理业务逻辑
│
├── utils/                      # 工具函数库
│   ├── __init__.py
│   ├── excel_db.py            # Excel数据库操作工具
│   ├── image_utils.py         # 图像处理工具
│   ├── jwt_utils.py           # JWT令牌工具
│   └── wechat_api.py          # 微信API接口工具
│
├── static/                     # 静态文件存储
│   ├── avatars/               # 用户头像存储目录
│   └── recipes/               # 菜谱图片存储目录
│
├── data/                       # 数据文件
│   └── database.xlsx          # Excel数据库文件
│
├── 接口文档/                   # API接口文档
│   ├── 用户登录接口.md
│   ├── 用户信息更新和头像上传接口.md
│   ├── 食物图像识别接口.md
│   ├── 食材库存列表接口.md
│   ├── 食材库存统计接口.md
│   ├── 更新食材接口.md
│   ├── 删除食材接口.md
│   ├── 最快过期食材接口.md
│   ├── 最快过期食材列表接口.md
│   ├── 基于过期食材匹配菜谱接口.md
│   ├── 菜谱推荐接口.md
│   └── 菜谱详情接口.md
│
├── 数据库设计/                 # 数据库设计文档
│   └── 数据库表名和字段.md
│
└── 豆包AI API接入文档/         # AI集成文档
    └── 豆包视觉模型.md
```

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- pip 包管理器
- 推荐使用虚拟环境

### 安装步骤

1. **克隆项目代码**
   ```bash
   git clone [仓库地址]
   cd 食光机-后端
   ```

2. **创建虚拟环境**（推荐）
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **安装项目依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置环境变量**
   
   创建 `.env` 文件或设置系统环境变量：
   ```env
   # 必需的环境变量（参考config.py中的配置）
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-key-here
   WECHAT_APPID=your-wechat-appid
   WECHAT_SECRET=your-wechat-secret
   DOUBAO_API_KEY=your-doubao-api-key
   ```
   
   **注意**：如果不设置环境变量，系统会使用 `config.py` 中的默认占位符值，但这些值无法正常工作，请务必配置真实的API密钥。

5. **初始化数据库**
   
   首次运行时会自动创建Excel数据库文件和必要的目录结构。

6. **启动应用**
   ```bash
   # 开发模式
   python app.py
   
   # 生产模式
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

7. **验证安装**
   
   访问 `http://localhost:5000` 确认服务正常运行。

## 📊 数据库设计

### 核心数据表

#### 1. 用户表 (users)
| 字段名 | 类型 | 描述 | 示例 |
|--------|------|------|------|
| id | 数字 | 主键，自增 | 1 |
| user_id | 文本 | 用户唯一标识 | u_12345678 |
| openid | 文本 | 微信openid | wx123456789 |
| nickname | 文本 | 用户昵称 | 张三 |
| avatar_url | 文本 | 头像URL | /static/avatars/xxx.jpg |
| health_goal | 文本 | 健康目标 | 减肥、增肌、均衡 |
| created_at | 日期时间 | 创建时间 | 2024-03-17 10:30:00 |

#### 2. 食材表 (ingredients)
| 字段名 | 类型 | 描述 | 示例 |
|--------|------|------|------|
| id | 数字 | 主键，自增 | 1 |
| name | 文本 | 食材名称 | 胡萝卜 |
| category | 文本 | 食材分类 | 蔬菜 |
| unit | 文本 | 计量单位 | 个、克、千克 |
| image | 文本 | 食材图片URL | /static/ingredients/carrot.jpg |
| description | 文本 | 营养描述 | 富含胡萝卜素 |

#### 3. 用户食材库存表 (user_ingredients)
| 字段名 | 类型 | 描述 | 示例 |
|--------|------|------|------|
| id | 数字 | 主键，自增 | 1 |
| user_id | 数字 | 用户ID（外键） | 1 |
| ingredient_id | 数字 | 食材ID（外键） | 1 |
| quantity | 数字 | 库存数量 | 500 |
| expiry_date | 日期 | 过期日期 | 2024-03-20 |
| created_at | 日期时间 | 添加时间 | 2024-03-17 |

#### 4. 菜谱表 (recipes)
| 字段名 | 类型 | 描述 | 示例 |
|--------|------|------|------|
| id | 数字 | 主键，自增 | 1 |
| name | 文本 | 菜谱名称 | 胡萝卜炒肉 |
| cook_time | 数字 | 烹饪时间(分钟) | 30 |
| calories | 数字 | 卡路里(千卡) | 350 |
| difficulty | 数字 | 难度等级(1-5) | 2 |
| steps | 文本 | 制作步骤(JSON) | [{"step":1,"desc":"切菜"}] |
| image | 文本 | 菜谱图片 | /static/recipes/dish.jpg |

#### 5. 菜谱食材关联表 (recipe_ingredients)
| 字段名 | 类型 | 描述 | 示例 |
|--------|------|------|------|
| id | 数字 | 主键，自增 | 1 |
| recipe_id | 数字 | 菜谱ID（外键） | 1 |
| ingredient_id | 数字 | 食材ID（外键） | 1 |
| quantity | 数字 | 所需数量 | 200 |
| unit | 文本 | 计量单位 | 克 |

## 🔌 API接口概览

### 用户管理接口

- `POST /api/login` - 微信小程序登录
- `PUT /api/user/profile` - 更新用户信息
- `POST /api/user/avatar` - 上传用户头像

### 食材管理接口

- `GET /api/ingredients` - 获取食材库存列表
- `POST /api/ingredients` - 添加食材到库存
- `PUT /api/ingredients/<id>` - 更新食材库存信息
- `DELETE /api/ingredients/<id>` - 删除食材库存
- `GET /api/ingredients/stats` - 获取食材库存统计
- `GET /api/ingredients/expiring` - 获取即将过期食材
- `GET /api/ingredients/expiring/top` - 获取最快过期食材

### 菜谱相关接口

- `GET /api/recipes/recommend` - 获取个性化菜谱推荐
- `GET /api/recipes/<id>` - 获取菜谱详细信息
- `GET /api/recipes/expiring-match` - 基于过期食材匹配菜谱

### AI图像识别接口

- `POST /api/image/recognize` - 食物图像智能识别

### 接口特性

- **统一响应格式**：所有接口返回统一的JSON格式
- **JWT身份验证**：安全的token认证机制
- **错误处理**：完善的错误信息和状态码
- **参数验证**：严格的请求参数校验
- **日志记录**：详细的操作日志记录

详细的API文档请参考 `接口文档/` 目录下的相关文件。

## 🤖 AI功能详解

### 豆包AI视觉识别

**模型信息**：
- 模型名称：doubao-1-5-vision-pro-32k-250115
- API提供商：字节跳动豆包AI
- 识别能力：多食材检测、数量估算、营养分析

**识别功能**：
1. **多食材检测**：单张图片可识别多种食材
2. **数量估算**：智能估算每种食材的数量
3. **置信度评估**：为每个识别结果提供可信度分数
4. **营养信息**：提供食材的营养价值说明
5. **保存建议**：预估食材的保存时间
6. **趣味知识**：为每种食材提供有趣的科普信息
7. **菜谱推荐**：基于识别结果推荐相关菜谱

**返回数据结构**：
```json
{
  "success": true,
  "ingredients": [
    {
      "name": "番茄",
      "quantity": 2,
      "unit": "个",
      "confidence": "92%",
      "storage_days": 7,
      "fun_fact": "番茄最初被欧洲人当作观赏植物",
      "tip": "冷冻后更易去皮",
      "emoji": "🍅",
      "health_note": "富含番茄红素，抗氧化"
    }
  ],
  "recipes": [
    {
      "name": "西红柿炒鸡蛋",
      "match_rate": "95%"
    }
  ],
  "summary": "根据图片共识别出2种食材"
}
```

## 🎯 推荐算法

### 菜谱推荐策略

1. **食材匹配度计算**
   - 计算用户拥有食材与菜谱所需食材的匹配程度
   - 考虑食材数量是否充足
   - 生成匹配度百分比

2. **临期食材优先**
   - 优先推荐使用即将过期食材的菜谱
   - 根据过期时间设置紧急度权重
   - 帮助用户减少食物浪费

3. **个性化因子**
   - 考虑用户的健康目标
   - 结合用户的历史偏好
   - 适应不同的饮食习惯

4. **多维度排序**
   - 匹配度权重：60%
   - 临期食材权重：25%
   - 个人偏好权重：15%

## 🔧 配置说明

### 环境变量配置

| 变量名 | 必需 | 描述 | 默认值 |
|--------|------|------|--------|
| SECRET_KEY | 是 | Flask应用密钥 | - |
| JWT_SECRET_KEY | 是 | JWT签名密钥 | - |
| WECHAT_APPID | 是 | 微信小程序AppID | - |
| WECHAT_SECRET | 是 | 微信小程序Secret | - |
| DOUBAO_API_KEY | 是 | 豆包AI API密钥 | - |

### 应用配置

- **JWT过期时间**：30天
- **文件上传限制**：5MB
- **支持的图片格式**：JPEG、PNG、GIF
- **数据库文件**：data/database.xlsx

## 🚀 部署指南

### 开发环境部署

```bash
# 启动开发服务器
python app.py
```

### 生产环境部署

```bash
# 使用Gunicorn部署
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 后台运行
nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > app.log 2>&1 &
```

### Docker部署（可选）

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 📈 性能优化

### 数据库优化
- 使用pandas进行高效的数据处理
- 实现数据缓存机制
- 优化Excel读写操作

### API性能
- 实现接口响应缓存
- 优化图像处理流程
- 异步处理长时间任务

### 内存管理
- 及时释放大文件内存
- 优化DataFrame操作
- 控制并发请求数量

## 🔍 故障排除

### 常见问题

1. **微信登录失败**
   - 检查WECHAT_APPID和WECHAT_SECRET配置
   - 确认微信小程序域名配置正确

2. **图像识别失败**
   - 验证DOUBAO_API_KEY是否有效
   - 检查网络连接和API配额

3. **Excel数据库错误**
   - 确认data目录有写入权限
   - 检查Excel文件是否被其他程序占用

4. **静态文件访问失败**
   - 确认static目录存在且有读取权限
   - 检查文件路径配置是否正确

### 日志调试

```bash
# 查看应用日志
tail -f app.log

# 开启调试模式
export FLASK_ENV=development
python app.py
```

## 🤝 贡献指南

### 开发规范

1. **代码风格**：遵循PEP 8规范
2. **注释要求**：关键函数必须有详细注释
3. **测试覆盖**：新功能需要编写对应测试
4. **文档更新**：API变更需要更新相关文档

### 提交流程

1. Fork项目到个人仓库
2. 创建功能分支：`git checkout -b feature/new-feature`
3. 提交代码：`git commit -m "Add new feature"`
4. 推送分支：`git push origin feature/new-feature`
5. 创建Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看LICENSE文件了解详情。

## 📞 联系方式
- 问题反馈：[GitHub Issues]

---

**注意**：本项目仅供学习和研究使用，请勿用于商业用途。使用前请确保已获得相关API服务的授权。

