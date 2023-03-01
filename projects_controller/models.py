from django.db import models

# Create your models here.
from django.db import models
from tools.basemodels import BaseModel


# 项目相关
class ProjectsController(BaseModel):
    project_type = models.CharField(null=True, max_length=200, blank=True, verbose_name='定制化或者主线')
    products_name = models.CharField(null=True, max_length=200, blank=True, verbose_name='产品名称')
    products_install_type = models.CharField(null=True, max_length=200, blank=True, verbose_name='部署类型')
    t_remark = models.CharField(null=True, max_length=200, blank=True, verbose_name='备注2')
    m_remark = models.CharField(null=True, max_length=200, blank=True, verbose_name='备注3')
    p_remark = models.CharField(null=True, max_length=200, blank=True, verbose_name='备注4')

    class Meta:
        db_table = 'projects_controller'
        ordering = ['-id']
        unique_together = ['name']
