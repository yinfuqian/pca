# -*- coding: utf-8 -*-
# @Time : 2023/1/16 12:42
# @Author : yinfuqian
# @File : urls.py
# @Project : manage.py

from django.urls import re_path, path
from . import views
from .views import *

urlpatterns = [
    re_path('machine_room/list/', MachineRoomsList.as_view(), name='machine_rooms_List'),
    re_path('machine_room/create/', MachineRoomsCreate.as_view(), name='machine_rooms_create'),
    re_path('machine_root/update/', MachineRoomsUpdate.as_view(), name='machine_rooms_update'),
    re_path('machine_root/delete/', MachineRoomsDelete.as_view(), name='machine_rooms_delete'),
    re_path('machine_cup/list/', MachineCupList.as_view(), name='machine_cup_list'),
    re_path('machine_cup/create/', MachineCupCreate.as_view(), name='machine_cup_create'),
    re_path('machine_cup/update/', MachineCupUpdate.as_view(), name='machine_cup_update'),
    re_path('machine_cup/delete/', MachineCupDelete.as_view(), name='machine_cup_delete'),
    re_path('machine_cup/search/', MachineCupSearch.as_view(), name='machine_cup_search'),
]
