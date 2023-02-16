import datetime
import time
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import *
from django.shortcuts import render, HttpResponse
from django.http import request, JsonResponse


# 云平台列表
class CloudTypeControllerListView(View):

    def get(self, request):
        data = CloudTypeController.objects.all().order_by('pk')
        return render(request, 'cloud_type_controller/cloud_cap_list.html', {'data': data})


# 云平台创建
class CloudTypeControllerCreateView(TemplateView):
    template_name = 'cloud_type_controller/cloud_cap_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = CloudTypeController()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# 云平台更新
class CloudTypeControllerUpdateView(TemplateView):
    def get(self, request):
        data = request.GET
        return render(request, 'cloud_type_controller/cloud_cap_update.html',
                      {'cloud_obj': CloudTypeController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            CloudTypeController.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                         updated_tm=datetime.datetime.now().strftime(
                                                                             '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# 云平台搜索
class CloudTypeControllerSearchView(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'cloud_type_controller/cloud_cap_search.html',
                          {'info': CloudTypeController.objects.get(name=request.GET.get('could_cap_search'))})
        except Exception as e:
            print(e)
            return render(request, 'cloud_type_controller/cloud_cap_list.html')


# 云平台删除
class CloudTypeControllerDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudTypeController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudTypeController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


# 服务器列表
class CloudServersControllerListView(ListView):
    template_name = 'cloud_servers_controller/cloud_servers_list.html'
    model = CloudServersController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(CloudServersControllerListView, self).get_context_data(**kwargs)
        context['page_range'] = self.page_range(context['page_obj'], context['paginator'])
        print(context)
        return context

    def page_range(self, page_obj, paginator):
        current_page = page_obj.number
        start = current_page - 2
        end = current_page + 3
        if start < 1:
            start = 1
        if end > paginator.num_pages:
            end = paginator.num_pages + 1
        return range(start, end)


# 服务器搜索
class CloudServersControllerSearchView(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'cloud_servers_controller/cloud_servers_search.html', {
                'info': CloudServersController.objects.get(
                    cloud_server_cloud_id=request.GET.get('cloud_servers_search'))})
        except Exception as e:
            print(e)
            return render(request, 'cloud_servers_controller/cloud_servers_list.html')


# 服务器更多信息
class CloudServersControllerInfoView(View):

    def get(self, request):
        data = CloudServersController.objects.filter(id=request.GET.get('id'))
        return render(request, 'cloud_servers_controller/cloud_server_info.html', {'data': data})


# 服务器创建
class CloudServersControllerCreateView(TemplateView):
    template_name = 'cloud_servers_controller/cloud_server_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        print(data)
        try:
            cloud = CloudServersController()
            cloud.cloud_server_project_type = data.get('cloud_server_project_type')  # 业务类型
            cloud.cloud_server_cost_env = data.get('cloud_server_cost_env')  # 成本归属
            cloud.cloud_server_check = data.get('cloud_server_check')  # 是否核对
            cloud.cloud_server_login_type = data.get('cloud_server_login_type')  # 登录方式
            cloud.cloud_server_cloud_belong = data.get('cloud_server_cloud_belong')  # 云归属
            cloud.cloud_server_city = data.get('cloud_server_city')  # 地域
            cloud.cloud_server_cloud_id = data.get('cloud_server_cloud_id')  # 实例id
            # IP相关
            cloud.cloud_server_ssh_ip = data.get('cloud_server_ssh_ip')
            cloud.cloud_server_pub_ip = data.get('cloud_server_pub_ip')
            cloud.cloud_server_owner = data.get('cloud_server_owner')  # 责任人
            cloud.cloud_server_env_type = data.get('cloud_server_env_type')  # 项目环境
            cloud.cloud_server_cloud_type = data.get('cloud_server_cloud_type')  # 公有云版本
            cloud.cloud_server_project_region = data.get('cloud_server_project_region')  # 项目区域
            cloud.cloud_server_project_env = data.get('cloud_server_project_env')  # 项目归属
            cloud.cloud_server_number = data.get('cloud_server_number')  # 项目编号
            cloud.cloud_server_all_name = data.get('cloud_server_all_name')  # 项目名称
            cloud.cloud_server_cost_money = data.get('cloud_server_cost_money')  # 月成本
            cloud.cloud_product_type = data.get('cloud_product_type')  # 产品类型
            cloud.cloud_server_cloud_name = data.get('cloud_server_cloud_name')  # 公有云实例名
            # 硬件资源
            cloud.cloud_server_cpus = data.get('cloud_server_cpus')
            cloud.cloud_server_mem = data.get('cloud_server_mem')
            cloud.cloud_server_cpus_car = data.get('cloud_server_cpus_car')
            cloud.cloud_server_sys_disks = data.get('cloud_server_sys_disks')
            cloud.cloud_server_data_disks = data.get('cloud_server_data_disks')
            cloud.cloud_server_status = data.get('cloud_server_status')  # 状态
            # 时间相关
            cloud.cloud_server_expiration_time = data.get('cloud_server_expiration_time')
            cloud.created_tm = data.get('cloud_server_create_time')
            # 备注
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.cloud_server_mark_tmp_2 = data.get('t_remark')
            cloud.cloud_server_mark_tmp_3 = data.get('m_remark')
            cloud.cloud_server_mark_tmp_4 = data.get('p_remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# 服务器状态修改
class CloudServersControllerStatusUpdateView(View):
    def get(self, request):
        data = request.GET
        res = {'status': 0}

        cloud = CloudServersController.objects.get(id=data.get('id'))

        # 0
        status = cloud.cloud_server_status

        print(data.get('name'))

        if status == "0":
            new_status = "1"
        else:
            new_status = "0"
        try:
            cloud = CloudServersController.objects.get(id=data.get('id'))
            cloud.cloud_server_status = new_status
            cloud.save()

        except Exception as e:
            print(e)
            res = {'status': 1}
        return JsonResponse(res)


# 服务器删除
class CloudServersControllerDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudServersController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudServersController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


# 服务器更新
class CloudServersControllerUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'cloud_servers_controller/cloud_server_update.html',
                      {'cloud_obj': CloudServersController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        # print(data)
        res = {'status': 0, 'msg': '更新成功'}
        id = data.get('id')
        a = list(CloudServersController.objects.filter(id=id).values("cloud_server_expiration_time"))
        b = a[0]
        now_ex_time = b["cloud_server_expiration_time"]
        try:
            # print(data)
            cloud_server_project_type = data.get('cloud_server_project_type')  # 业务类型
            cloud_server_cost_env = data.get('cloud_server_cost_env')  # 成本归属
            cloud_server_check = data.get('cloud_server_check')  # 是否核对
            cloud_server_login_type = data.get('cloud_server_login_type')  # 登录方式
            cloud_server_cloud_belong = data.get('cloud_server_cloud_belong')  # 云归属
            cloud_server_city = data.get('cloud_server_city')  # 地域
            # cloud_server_cloud_id = data.get('cloud_server_cloud_id')  # 实例id
            # IP相关
            cloud_server_ssh_ip = data.get('cloud_server_ssh_ip')
            cloud_server_pub_ip = data.get('cloud_server_pub_ip')
            cloud_server_owner = data.get('cloud_server_owner')  # 责任人
            cloud_server_env_type = data.get('cloud_server_env_type')  # 项目环境
            cloud_server_cloud_type = data.get('cloud_server_cloud_type')  # 公有云版本
            cloud_server_project_region = data.get('cloud_server_project_region')  # 项目区域
            cloud_server_project_env = data.get('cloud_server_project_env')  # 项目归属
            cloud_server_number = data.get('cloud_server_number')  # 项目编号
            cloud_server_all_name = data.get('cloud_server_all_name')  # 项目名称
            cloud_server_cost_money = data.get('cloud_server_cost_money')  # 月成本
            cloud_product_type = data.get('cloud_product_type')  # 产品类型
            cloud_server_cloud_name = data.get('cloud_server_cloud_name')  # 公有云实例名

            # 硬件资源
            cloud_server_cpus = data.get('cloud_server_cpus')
            cloud_server_mem = data.get('cloud_server_mem')
            cloud_server_cpus_car = data.get('cloud_server_cpus_car')
            cloud_server_sys_disks = data.get('cloud_server_sys_disks')
            cloud_server_data_disks = data.get('cloud_server_data_disks')
            cloud_server_status = data.get('cloud_server_status')  # 状态
            # 时间相关
            if data.get('cloud_server_expiration_time') == now_ex_time:
                cloud_server_expiration_time = data.get('cloud_server_expiration_time')
            else:
                cloud_server_expiration_time = data.get('cloud_server_expiration_time')
                year = cloud_server_expiration_time.split("年")[0]
                month = cloud_server_expiration_time.split("年")[1].split("月")[0]
                day = cloud_server_expiration_time.split("年")[1].split("月")[1].split("日")[0]
                cloud_server_expiration_time = year + "-" + month + "-" + day
            # 备注
            remark = data.get('remark')
            cloud_server_mark_tmp_2 = data.get('t_remark')
            cloud_server_mark_tmp_3 = data.get('m_remark')
            cloud_server_mark_tmp_4 = data.get('p_remark')
            CloudServersController.objects.filter(id=data.get("id")).update(
                cloud_server_project_type=cloud_server_project_type,
                cloud_server_cost_env=cloud_server_cost_env,
                cloud_server_check=cloud_server_check,
                cloud_server_login_type=cloud_server_login_type,
                cloud_server_cloud_belong=cloud_server_cloud_belong,
                cloud_server_city=cloud_server_city,
                cloud_server_ssh_ip=cloud_server_ssh_ip,
                cloud_server_pub_ip=cloud_server_pub_ip,
                cloud_server_owner=cloud_server_owner,
                cloud_server_env_type=cloud_server_env_type,
                cloud_server_cloud_type=cloud_server_cloud_type,
                cloud_server_project_region=cloud_server_project_region,
                cloud_server_project_env=cloud_server_project_env,
                cloud_server_number=cloud_server_number,
                cloud_server_all_name=cloud_server_all_name,
                cloud_server_cost_money=cloud_server_cost_money,
                cloud_product_type=cloud_product_type,
                cloud_server_cloud_name=cloud_server_cloud_name,
                cloud_server_cpus=cloud_server_cpus,
                cloud_server_mem=cloud_server_mem,
                cloud_server_cpus_car=cloud_server_cpus_car,
                cloud_server_sys_disks=cloud_server_sys_disks,
                cloud_server_data_disks=cloud_server_data_disks,
                cloud_server_expiration_time=cloud_server_expiration_time,
                cloud_server_status=cloud_server_status,
                remark=remark,
                cloud_server_mark_tmp_2=cloud_server_mark_tmp_2,
                cloud_server_mark_tmp_3=cloud_server_mark_tmp_3,
                cloud_server_mark_tmp_4=cloud_server_mark_tmp_4,
                updated_tm=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)
