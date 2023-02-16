from django.db import models
from tools.basemodels import BaseModel

# Create your models here.

"""
项目组类型
运维公共项目/AIBPO业务中心...
"""


class PcaProductGroupsController(BaseModel):
    class Meta:
        db_table = 'pca_product_groups_controller'
        ordering = ['-id']
        unique_together = ['name']


"""
产品类型
yibot/call/see
"""


class PcaProjectType(BaseModel):
    class Meta:
        db_table = 'pca_project_type'
        ordering = ['-id']
        unique_together = ['name']


"""
公有云版本类型
POC/多客户..
"""


class CloudVersionController(BaseModel):
    class Meta:
        db_table = 'cloud_version_controller'
        ordering = ['-id']
        unique_together = ['name']


"""
环境类型管理
Prod/POC/test/dev/sit
"""


class PcaProjectEnvController(BaseModel):
    class Meta:
        db_table = 'pca_project_env_controller'
        ordering = ['-id']
        unique_together = ['name']


"""
项目环境/项目归属/项目简称_项目编码
Prod/POC/test/dev/sit
"""


class PcaProjectBelongController(BaseModel):
    class Meta:
        db_table = 'pca_project_belong_controller'
        ordering = ['-id']
        unique_together = ['name']
