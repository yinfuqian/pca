from django.db import models

# Create your models here.
from tools.basemodels import BaseModel
from dashboard.models import *

"""
硬件资产管理
"""

"""
机房
"""


class StaticRooms(BaseModel):
    class Meta:
        db_table = 'static_rooms'
        unique_together = ['name']


"""
机柜
"""


class StaticEqcabs(BaseModel):
    static_room_name = models.CharField(default="", null=False, max_length=50, verbose_name="归属机房")
    class Meta:
        db_table = "static_eqcabs"
        unique_together = ['name']


"""
网络
"""


class StaticNetWorks(BaseModel):
    class Meta:
        db_table = 'static_network'
        ordering = ['-id']
        unique_together = ['name']


"""
服务器
"""

class StaticServers(BaseModel):
    STATUS = (
        ('0', u'下线'),
        ('1', u'在线'),
        ('2', u'关机'),
    )
    static_server_login_type = models.CharField(default="", null=True, max_length=50, verbose_name="登陆方式")
    static_server_ssh_ip = models.CharField(default="", null=True, max_length=50, verbose_name="内网SSH地址")
    static_server_mark_tmp = models.CharField(default="", null=True, max_length=50, verbose_name="临时备注")
    static_server_status = models.CharField(default='1', max_length=2, choices=STATUS, verbose_name='运行状态')
    static_server_cpus = models.PositiveBigIntegerField(default='', null=True, verbose_name='cpu')
    static_server_cpus_car = models.PositiveBigIntegerField(default='', null=True,  verbose_name='cpu卡数')
    static_server_mems = models.PositiveBigIntegerField(default='', null=True, verbose_name='内存')
    static_server_sysdisks = models.PositiveBigIntegerField(default='', null=True, verbose_name='系统盘')
    static_server_datadisks = models.PositiveBigIntegerField(default='', null=True, verbose_name='数据盘')

    class Meta:
        ordering = ['id']
