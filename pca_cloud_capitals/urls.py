from django.conf.urls import include
from django.urls import re_path, path
from .views import *

urlpatterns = [
    re_path(r'cloud/list', CloudTypeControllerListView.as_view(), name='cloud_cap_list'),
    re_path(r'cloud/create', CloudTypeControllerCreateView.as_view(), name='cloud_cap_create'),
    re_path(r'cloud/update', CloudTypeControllerUpdateView.as_view(), name='cloud_cap_update'),
    re_path(r'cloud/delete', CloudTypeControllerDeleteView.as_view(), name='cloud_cap_delete'),
    re_path(r'cloud/search', CloudTypeControllerSearchView.as_view(), name='could_cap_search'),
    re_path(r'servers/list/info', CloudServersControllerInfoView.as_view(), name='cloud_servers_info'),
    re_path('servers/list/', CloudServersControllerListView.as_view(), name='cloud_servers_list'),
    re_path('servers/create', CloudServersControllerCreateView.as_view(), name='cloud_servers_create'),
    re_path('servers/status', CloudServersControllerStatusUpdateView.as_view(), name='cloud_servers_status'),
    re_path('servers/delete', CloudServersControllerDeleteView.as_view(), name='cloud_servers_delete'),
    re_path('servers/update', CloudServersControllerUpdateView.as_view(), name='cloud_servers_update'),
    re_path('servers/search', CloudServersControllerSearchView.as_view(), name='cloud_servers_search'),
]
