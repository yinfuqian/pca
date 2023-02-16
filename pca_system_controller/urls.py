# -*- coding: utf-8 -*-
# @Time : 2023/2/15 10:22
# @Author : yinfuqian
# @File : urls.py
# @Project : pca
from django.conf.urls import include
from django.urls import re_path
from .views import *
urlpatterns = [
    re_path('list/',  UserListView.as_view(), name='user_list'),
    re_path('create/', UserAddView.as_view(), name='user_create'),
    re_path('delete/', UserDeleteView.as_view(), name='user_delete'),
    re_path('update/', UserUpdateView.as_view(), name='user_update'),
    re_path('status/', UserStatus.as_view(), name='user_status'),
    re_path('ssh/', SSHListView.as_view(), name='ssh_list'),
    re_path('search/', UserSearch.as_view(), name='user_search'),
]