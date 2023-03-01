# -*- coding: utf-8 -*-
# @Time : 2023/1/11 15:18
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py


from django.conf.urls import include
from django.urls import re_path, path
from .views import *
from projects_controller.views import *

urlpatterns = [
    re_path(r'projects_controller/list/', ProjectsControllerListView.as_view(), name='project_controller_list'),
    re_path(r'projects_controller/update/', ProjectsControllerUpdataView.as_view(), name='project_controller_update'),
    re_path(r'projects_controller/delete/', ProjectsControllerDeleteView.as_view(), name='project_controller_delete'),
    re_path(r'projects_controller/create/', ProjectsControllerCreateView.as_view(), name='project_controller_create'),
    re_path(r'projects_controller/search/', ProjectsControllerSearchView.as_view(), name='project_controller_search'),
    re_path(r'projects_controller/more/', ProjectsControllerMoreView.as_view(), name='project_controller_more'),
    # 项目组管理
    re_path(r'project_groups/list/', BusProjectsGroupListView.as_view(), name='projects_groups_list'),
    re_path(r'project_groups/update/', BusProjectsGroupUpdateView.as_view(), name='projects_groups_update'),
    re_path(r'project_groups/delete/', BusProjectsGroupDeleteView.as_view(), name='projects_groups_delete'),
    re_path(r'project_groups/create/', BusProjectsGroupCreateView.as_view(), name='projects_groups_create'),
    re_path(r'project_groups/search/', BusProjectsGroupSearchView.as_view(), name='projects_groups_search'),
    # 　产品管理
    re_path(r'products/list/', ProductTypeListView.as_view(), name='product_type_list'),
    re_path(r'products/update/', ProductTypeUpdateView.as_view(), name='product_type_update'),
    re_path(r'products/delete/', ProductTypeDeleteView.as_view(), name='product_type_delete'),
    re_path(r'products/create/', ProductTypeCreateView.as_view(), name='product_type_create'),
    re_path(r'products/search/', ProductTypeSearchView.as_view(), name='product_type_search'),
    # 公有云版本管理
    re_path(r'cloud_version/list/', CloudVersionListView.as_view(), name='cloud_version_list'),
    re_path(r'cloud_version/update/', CloudVersionUpdateView.as_view(), name='cloud_version_update'),
    re_path(r'cloud_version/delete/', CloudVersionDeleteView.as_view(), name='cloud_version_delete'),
    re_path(r'cloud_version/create/', CloudVersionCreateView.as_view(), name='cloud_version_create'),
    re_path(r'cloud_version/search/', CloudVersionSearchView.as_view(), name='cloud_version_search'),
    # 环境类型
    re_path(r'product_env_type/list/', ProductEnvTypeListView.as_view(), name='product_env_type_list'),
    re_path(r'product_env_type/update/', ProductEnvTypeUpdateView.as_view(), name='product_env_type_update'),
    re_path(r'product_env_type/delete/', ProductEnvTypeDeleteView.as_view(), name='product_env_type_delete'),
    re_path(r'product_env_type/create/', ProductEnvTypeCreateView.as_view(), name='product_env_type_create'),
    re_path(r'product_env_type/search/', ProductEnvTypeSearch.as_view(), name='product_env_type_search'),
    # 项目环境
    re_path(r'product_env/list/', ProductEnvListView.as_view(), name='product_env_list'),
    re_path(r'product_env/update/', ProductEnvUpdateView.as_view(), name='product_env_update'),
    re_path(r'product_env/delete/', ProductEnvDeleteView.as_view(), name='product_env_delete'),
    re_path(r'product_env/create/', ProductEnvCreateView.as_view(), name='product_env_create'),
    re_path(r'product_env/search/', ProductEnvSearchView.as_view(), name='product_env_search'),
]
