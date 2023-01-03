# UESTC跳蚤市场

## 提示

1. 下载
2. 打开文件夹
3. 打开VScode

4. 打开终端，输入命令:

```cmd
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
py manage.py runserver
```

> 若出现如下报错：
>
> OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: '<frozen importlib._bootstrap>' ，请检查requirements.txt中的package是否全部安装成功，如遇安装问题，可升级pip至最新版后再安装



## 管理员登录

1. 在普通用户使用的页面中没有添加进入管理页面的按钮，管理员可直接访问以下URL进入后台管理页面：http://127.0.0.1:8000/admin
2. 管理员账号和密码均为：admin



## 原型系统的功能实现情况

针对普通用户：

- [x] 用户注册（邮件验证）和登录
- [x] 账户管理，收件地址管理
- [x] 分类查看商品
- [x] 添加购物车
- [x] 添加心愿清单
- [x] 个人商品管理上传、更新和删除商品
- [x] 按名称搜索商品
- [x] 购买商品，选择运输方式和收件地址
- [x] 查看订单记录（分买家查看和卖家查看）
- [x] 发布评论



针对管理员：

- [x] 管理员登录
- [x] 管理所有商品
- [x] 管理所有用户



未实现的功能和bug：

注册时的密码格式检查不完善

输入位数正确但不存在的邮箱会导致系统崩溃

心愿清单仅实现了列表，未实现商品信息跟踪

未实现打折功能，打折价格未使用



Notice：

1. 级联删除，user，category是product的外键