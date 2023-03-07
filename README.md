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
----------------------------------------------------------分割线-----------------------------------------------
![image](https://user-images.githubusercontent.com/43942747/223389859-923c2254-33fe-4d9b-a386-a5cdc5f34c56.png)
![image](https://user-images.githubusercontent.com/43942747/223389886-30684764-e3be-4ac8-9bb8-8e2e84f9b195.png)
![image](https://user-images.githubusercontent.com/43942747/223389909-e9c2c902-fe26-4489-a7ab-2b2e7a6f7f37.png)
![image](https://user-images.githubusercontent.com/43942747/223389935-50b3b224-f0da-4ee5-93dc-36ee954d426c.png)
![image](https://user-images.githubusercontent.com/43942747/223389959-5629ecaf-84c7-4653-ad26-4f08b30e678f.png)
![image](https://user-images.githubusercontent.com/43942747/223389974-de4cf901-bc5b-4e72-91bc-cf1a7fe47802.png)
