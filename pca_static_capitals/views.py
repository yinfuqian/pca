import datetime

from django.http import JsonResponse, request, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import *


# Create your views here.
# 机房列表

class MachineRoomsList(View):
    def get(self, request):
        data = StaticRooms.objects.all().order_by('pk')
        return render(request, 'static_machine_rooms_controller/machine_rooms_list.html', {'data': data})


# 创建机房
class MachineRoomsCreate(TemplateView):
    template_name = 'static_machine_rooms_controller/machine_rooms_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            static_name = StaticRooms()
            static_name.name = data.get('name')
            static_name.remark = data.get('remark')
            static_name.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# 机房更新
class MachineRoomsUpdate(TemplateView):
    def get(self, request):
        data = request.GET
        return render(request, 'static_machine_rooms_controller/machine_rooms_update.html',
                      {'cloud_obj': StaticRooms.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            StaticRooms.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                 updated_tm=datetime.datetime.now().strftime(
                                                                     '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# 机房删除

class MachineRoomsDelete(View):
    def get(self, request):
        data = request.GET
        cloud = StaticRooms()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            StaticRooms.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


#  机柜列表
class MachineCupList(View):
    def get(self, request):
        data = StaticEqcabs.objects.all().order_by('pk')
        return render(request, 'static_machine_cup_controller/machine_cup_list.html', {'data': data})


# 创建机柜
class MachineCupCreate(TemplateView):
    template_name = 'static_machine_cup_controller/machine_cup_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            static_name = StaticEqcabs()
            static_name.name = data.get('name')
            static_name.static_room_name = data.get('static_room_name')
            static_name.remark = data.get('remark')
            static_name.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# 机房更新
class MachineCupUpdate(TemplateView):
    def get(self, request):
        data = request.GET
        return render(request, 'static_machine_cup_controller/machine_cup_update.html',
                      {'cloud_obj': StaticEqcabs.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            static_room_name = data.get('static_room_name')
            StaticEqcabs.objects.filter(id=data.get("id")).update(name=name, remark=remark, static_room_name=static_room_name,
                                                            updated_tm=datetime.datetime.now().strftime(
                                                                '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# 机柜删除

class MachineCupDelete(View):
    def get(self, request):
        data = request.GET
        cloud = StaticRooms()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            StaticEqcabs.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


# 　机柜搜索

class MachineCupSearch(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'static_machine_cup_controller/machine_cup_search.html',
                          {'info': StaticRooms.objects.get(name=request.GET.get('machine_cup_search'))})
        except Exception as e:
            print(e)
            return render(request, 'static_machine_cup_controller/machine_cup_list.html')
