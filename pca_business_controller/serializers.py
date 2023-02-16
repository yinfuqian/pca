# -*- coding: utf-8 -*-
# @Time : 2023/1/12 9:55
# @Author : yinfuqian
# @File : serializers.py
# @Project : manage.py
from rest_framework import serializers
from .models import *
from pca_cloud_capitals.models import *


# 项目组
class ProjectGroupModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcaProductGroupsController
        fields = "__all__"


# 产品类型
class ProductTypeModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcaProjectType
        fields = "__all__"


# 环境类型
class CloudEnvTypeModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcaProjectEnvController
        fields = "__all__"


# 项目环境
class PcaProjectBelongControllerModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcaProjectBelongController
        fields = "__all__"


# 公有云版本
class CloudVersionModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudVersionController
        fields = "__all__"
