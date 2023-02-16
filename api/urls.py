# -*- coding: utf-8 -*-
# @Time : 2023/1/11 10:31
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py

from django.urls import re_path, path
from . import views

urlpatterns = [
    path("userlist/", views.APIUserList.as_view({'get': 'list'})),  # 用户列表
    path("cloudlist/", views.APICloudList.as_view({'get': 'list'})),  # 云列表
    path("project_group_list/", views.APIProjectGroupList.as_view({'get': 'list'})),  # 项目组
    path("product_type_list/", views.APIProductTypeList.as_view({'get': 'list'})),  # 产品类型
    path("server_env_type_list/", views.APIServerEnvTypeList.as_view({'get': 'list'})),  # 环境类型
    path("cloud_version_list/", views.APICloudVersionList.as_view({'get': 'list'})),  # 公有云版本
    path("product_env_type_list/", views.APICloudEnvTypeList.as_view({'get': 'list'})),  # 项目环境、项目归属
    path("macine_rooms_list/", views.APIMachineRoomsList.as_view({'get': 'list'})),  # 机柜
]
