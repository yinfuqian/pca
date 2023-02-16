from django.db import models
from tools.basemodels import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.
"""
用户表
"""
class PcaUserController(AbstractUser):
    ROLES = (
        ('dev-adm', u'超级管理员'),
        ('dev-manage', u'运维'),
        ('dev-devlop', u'普通用户'),
        ('dev-pm', u'PM'),
        ('dev-tm', u'TM')
    )
    id = models.AutoField(help_text="用户名", primary_key=True)
    username = models.CharField(max_length= 200, help_text="用户名", unique=True)
    phone = models.CharField(max_length=11, verbose_name='手机号', unique=True, null=True)
    password = models.SlugField(max_length=128, help_text="用户密码")
    role = models.CharField(max_length=32, default='dev-manage', choices=ROLES)
    # 指定数据库表信息
    class Meta:
        ordering = ['-id']
        db_table = 'pca_user_controller'
        verbose_name = '系统用户'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

"""
SSH 用户
"""
class PcaSshUserController(BaseModel):
    STATUS = (
        ('0', u'启用'),
        ('1', u'弃用'),
    )
    password = models.CharField(default='', max_length=128, null=True, blank=True, verbose_name='SSH 密码')

    class Meta:
        db_table = 'pca_ssh_user_controller'
        ordering = ['-id']
        unique_together = ['name']


