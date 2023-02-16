from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from pca_cloud_capitals.models import *
from pca_system_controller.models import *
from pca_system_controller.serializers import AccountModeleSerializer
from pca_cloud_capitals.serializers import CloudModeleSerializer
from pca_business_controller.serializers import *
from pca_static_capitals.serializers import *


# Create your views here.

# 用户列表
class APIUserList(viewsets.ModelViewSet):
    queryset = PcaUserController.objects.all()
    serializer_class = AccountModeleSerializer

# 云类型列表
class APICloudList(viewsets.ModelViewSet):
    queryset = CloudTypeController.objects.all()
    serializer_class = CloudModeleSerializer

# 项目组
class APIProjectGroupList(viewsets.ModelViewSet):
    queryset = PcaProductGroupsController.objects.all()
    serializer_class = ProjectGroupModeleSerializer

# 产品类型
class APIProductTypeList(viewsets.ModelViewSet):
    queryset = PcaProjectType.objects.all()
    serializer_class = ProductTypeModeleSerializer

# 环境类型
class APIServerEnvTypeList(viewsets.ModelViewSet):
    queryset = PcaProjectEnvController.objects.all()
    serializer_class = CloudEnvTypeModeleSerializer

# 公有云版本
class APICloudVersionList(viewsets.ModelViewSet):
    queryset = CloudVersionController.objects.all()
    serializer_class = CloudVersionModeleSerializer

# 机柜
class APIMachineRoomsList(viewsets.ModelViewSet):
    queryset = StaticRooms.objects.all()
    serializer_class = MachineRoomsListSerializer

# 项目环境
class APICloudEnvTypeList(viewsets.ModelViewSet):
    queryset = PcaProjectBelongController.objects.all()
    serializer_class = PcaProjectBelongControllerModeleSerializer