# 102202135-102202146
# 目录说明和使用说明
#### 前端代码目录
```
Software_Engineering_JOB1 项目目录：

├── register
│   ├── id_test.vue            # 身份验证页面
│   ├── register.vue           # 用户注册页面
│   ├── register_fail.vue      # 注册失败的提示页面
│   └── register_success.vue   # 注册成功的提示页面
│
├── static                     # 静态资源目录
│   ├── avatars                # 用户头像文件
│   ├── icons                  # 图标资源
│   ├── login                  # 登录相关静态资源
│   └── photo                  # 照片文件
│
├── unpackage                  # 编译后生成的打包文件
│   └── dist                   # 打包后的项目文件
│
├── App.vue                    # Vue.js 应用的根组件
├── index.html                 # 应用的入口 HTML 文件
├── main.js                    # Vue.js 应用的入口 JavaScript 文件
├── manifest.json              # 应用的配置文件
├── pages.json                 # 页面路由信息
├── uni.promisify.adaptor.js   # Promise 适配器文件
└── uni.scss                   # 全局样式文件

├── pages                      # 页面目录
│   ├── find_project           # 与项目查找相关的页面
│   │   ├── find_project.vue   # 查找项目的页面
│   │   └── know_more.vue      # 了解更多项目细节的页面
│   │
│   ├── home                   # 主页和相关功能的页面
│   │   ├── find_friend.vue    # 查找好友的页面
│   │   ├── home.vue           # 主页页面
│   │   ├── look.vue           # 浏览页面
│   │   ├── project_setting.vue # 项目设置页面
│   │   ├── publish_project.vue # 发布项目页面
│   │   └── teammate.vue       # 团队成员页面
│   │
│   ├── login                  # 登录相关页面
│   │   ├── login.vue          # 登录页面
│   │   ├── password_different.vue # 密码不一致的提示页面
│   │   └── password_wrong.vue # 密码错误的提示页面
│   │
│   ├── message                # 消息相关页面
│   │   ├── contactDetail.vue  # 联系人详情页面
│   │   └── message.vue        # 消息页面
│   │
│   └── person                 # 用户个人相关页面
│       ├── about_us.vue       # 关于我们的页面
│       ├── account_security.vue # 账户安全设置页面
│       ├── donate.vue         # 捐赠页面
│       ├── feedback.vue       # 反馈页面
│       ├── person.vue         # 个人信息页面
│       ├── personal_info.vue  # 个人详细信息页面
│       └── system_settings.vue # 系统设置页面
```
####后端代码目录
```
102202135-102202146-main
│  manage.py                                      # Django项目的命令行工具，用于管理项目（如运行服务器、迁移数据库等）
│  README.md                                      # 项目说明文件，包含项目简介、安装指南、使用说明等
│
├─chat                                           # 聊天模块，处理用户之间的消息交流功能
│  │  admin.py                                    # 配置Django admin界面，注册聊天模型以便在后台管理
│  │  apps.py                                     # 配置聊天应用的配置类
│  │  models.py                                   # 定义聊天模块的数据模型（如PrivateMessage, ChatInvitation）
│  │  tests.py                                    # 聊天模块的单元测试
│  │  urls.py                                     # 定义聊天模块的URL路由
│  │  views.py                                    # 定义处理聊天功能的视图函数或类视图
│  │  __init__.py                                 # 初始化聊天模块，使其成为一个Python包
│
├─media                                          # 媒体文件存储目录，用于存放用户上传的头像和项目相关文件
│  ├─avatars                                     # 用户头像图片存储目录
│  │  └─8                                         # 用户ID为8的头像存储文件夹
│  │          222874a9-fcc7-436b-b230-d752d438a283.jpg  # 用户8的头像图片
│  │
│  └─project_files                               # 项目相关文件存储目录
│      ├─project1                                 # 项目1的文件存储文件夹
│      │      image7.jpg                           # 项目1的相关图片文件
│      │
│      └─test-project                             # 测试项目的文件存储文件夹
│              test_file.txt                       # 测试项目的一个文本文件
│              test_file_fAdk5Xw.txt               # 测试项目的另一个文本文件
│              test_file_P4O0b0m.txt               # 测试项目的另一个文本文件
│              test_file_xgejsnB.txt               # 测试项目的另一个文本文件
│              test_file_YDdMb5p.txt               # 测试项目的另一个文本文件
│              test_file_YWEJG7F.txt               # 测试项目的另一个文本文件
│
├─partners                                       # 合作伙伴模块，管理和处理项目合作相关功能
│  │  asgi.py                                     # ASGI配置文件，用于部署Django应用（如异步通信）
│  │  settings.py                                 # 项目的全局设置文件，配置数据库、已安装应用、Middleware等
│  │  urls.py                                     # 定义项目级别的URL路由
│  │  wsgi.py                                     # WSGI配置文件，用于部署Django应用（如传统同步服务器）
│  │  __init__.py                                 # 初始化合作伙伴模块，使其成为一个Python包
│
├─projects                                       # 项目管理模块，处理项目的创建、编辑、删除以及项目成员的管理等功能
│  │  admin.py                                    # 配置Django admin界面，注册项目模型以便在后台管理
│  │  apps.py                                     # 配置项目应用的配置类
│  │  models.py                                   # 定义项目模块的数据模型（如Project, ProjectMember, ProjectFile）
│  │  permissions.py                              # 定义项目模块的权限控制
│  │  serializers.py                              # 定义项目模块的数据序列化类，用于API接口
│  │  tests.py                                    # 项目模块的单元测试
│  │  urls.py                                     # 定义项目模块的URL路由
│  │  views.py                                    # 定义处理项目功能的视图函数或类视图
│  │  __init__.py                                 # 初始化项目模块，使其成为一个Python包
│
└─users                                          # 用户管理模块，处理用户注册、登录、个人信息管理和账号安全等功能
    │  admin.py                                    # 配置Django admin界面，注册用户模型以便在后台管理
    │  apps.py                                     # 配置用户应用的配置类
    │  models.py                                   # 定义用户模块的数据模型（如User）
    │  tests.py                                    # 用户模块的单元测试
    │  urls.py                                     # 定义用户模块的URL路由
    │  views.py                                    # 定义处理用户功能的视图函数或类视图
    │  __init__.py                                 # 初始化用户模块，使其成为一个Python包
```
