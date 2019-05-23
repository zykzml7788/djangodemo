# djangodemo
用django开发的几个简单接口（注册，登入，注销，查询用户）

## 环境配置
- 使用pycharm打开
- 根据requirements.txt安装依赖包，可使用命令pip -r requirements.txt安装依赖

## 启动服务
- 在控制台输入  python manage.py runserver 0.0.0.0:8000  启动django

## 接口文档（因为swagger插件生成不了文档，暂时先手动整理）

接口地址 | 请求方式 | 入参 |  接口描述  
-|-|-|-
mock/register | POST | FROM-DATA格式：username,password,email | 注册接口 |
mock/login | POST | JSON格式：username,password | 登入接口，返回cookie |
mock/logout | POST |  | 注销接口，失效cookie |
mock/user/queryAll | GET |  | 查询所有注册用户（需登入） |
mock/user/query | POST | JSON格式:username | 查询单个用户信息（需登入） |
