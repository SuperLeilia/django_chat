# Django Chat & Stock Price Generation

## 包及组件安装
- Python包安装见requirements.txt
- Docker
----------
## 项目搭建
### 将终端进入到项目目录下
```
    cd your_path/django_chat/
```
### 执行 migration
```
    python manage.py migrate
```
### 启动项目
```
    python manage.py runserver
```
### 启动 redis

```
    docker run -p 6379:6379 -d redis:5
```

### 启动 Celery Worker

    celery -A django_chat worker -l info

### 启动 Celery beat

    celery -A django_chat beat -l info
----------
## 项目访问

- 主界面: http://127.0.0.1:8000/, 登陆后自动跳转到聊天室
- 登录：http://127.0.0.1:8000/login/
- 注册：http://127.0.0.1:8000/register/
- 个人信息: http://127.0.0.1:8000/profile/
- 聊天室: http://127.0.0.1:8000/chat/room
- WebSocket请求下股票数据推送: http://127.0.0.1:8000/stock/channel_room
- HTTP请求下股票数据推送: http://127.0.0.1:8000/stock/http_room
----------
## 主要模块

- Users: 用户的登录、注册、登出及个人信息
   1. 通过 users/forms.py 自定义表单验证
   2. 支持修改账户信息
   
- Chat: 聊天室，多用户实时聊天
   1. 不同浏览器多用户登录聊天室
   2. 支持用户进入/退出聊天室时的提醒功能
   3. 使用 Celery Task 实现聊天消息异步发送
   
- Stock: 定时任务推送股票价格
   1. 输入框输入股票代码，不断返回新生成的股票价格
   2. 支持输入框实时更新股票代码，直到输入"停止"结束发送
   3. 支持以 HTTP 请求与 Websocket 请求两种方式实现股票代码的发送
   4. Celery PeriodicTask 实现定时推送股票价格

