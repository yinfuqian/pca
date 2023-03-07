# 项目说明
## 版本说明
- python 1.11.1
- openssl 1.0.2k-fips
- pip 23.0
- mysql 5.7.41
- redis 暂无

## 安装说明
· 修改数据库配置
/pca/pca/settings.py
```angular2html
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pca',
        'USER': 'admin',
        'PASSWORD': 'admin1234',
        'HOST': '172.16.20.153',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    },
}

```
· 创建数据库
```angular2html
CREATE DATABASE IF NOT EXISTS pca DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
· 数据迁移
```angular2html
python3 manage.py makemigrations
python3 manage.py migrate
```
没有报错则正常
· 创建用户
```angular2html
python3　manage.py createsuperuser
```
· nginx 配置
```angular2html
server {
  	listen 80;
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
        add_header Access-Control-Allow-Headers 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
  	server_name 127.0.0.1:8000	;

  location / {
	proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_pass   http://0.0.0.0:8000;

}
}
```
## 启动说明
```angular2html
python3 manage.py runserver 
```
默认为8000 端口
## api
http://172.16.20.153/api/list

-------------------------------------------------------------------------------------------
![img_1.png](img_1.png)
![img_2.png](img_2.png)
![img_3.png](img_3.png)
![img_4.png](img_4.png)
![img_5.png](img_5.png)
![img_6.png](img_6.png)