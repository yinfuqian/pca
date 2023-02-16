import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import *
from pca_cloud_capitals.models import *

# Create your views here.


"""
项目组相关
列表/创建/删除/更新/搜索
"""


# list
class BusProjectsGroupListView(ListView):
    template_name = 'business_groups_controllers/business_group_list.html'
    model = PcaProductGroupsController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(BusProjectsGroupListView, self).get_context_data(**kwargs)
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


# update
class BusProjectsGroupUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'business_groups_controllers/business_group_update.html',
                      {'project_obj': PcaProductGroupsController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            PcaProductGroupsController.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                                updated_tm=datetime.datetime.now().strftime(
                                                                                    '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# delete
class BusProjectsGroupDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = PcaProductGroupsController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            PcaProductGroupsController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


# create
class BusProjectsGroupCreateView(TemplateView):
    template_name = 'business_groups_controllers/business_group_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = PcaProductGroupsController()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# search
class BusProjectsGroupSearchView(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'business_groups_controllers/business_group_search.html', {
                'info': PcaProductGroupsController.objects.get(name=request.GET.get('projects_groups_search'))})
        except Exception as e:
            print(e)
            return render(request, 'business_groups_controllers/business_group_list.html')


"""
公有云版本相关
列表/创建/删除/更新
"""

# list
class CloudVersionListView(ListView):
    template_name = 'cloud_version_controller/cloud_version_list.html'
    model = CloudVersionController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(CloudVersionListView, self).get_context_data(**kwargs)
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

# update
class CloudVersionUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'cloud_version_controller/cloud_version_update.html',
                      {'version_obj': CloudVersionController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            CloudVersionController.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                       updated_tm=datetime.datetime.now().strftime(
                                                                           '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)

# delete
class CloudVersionDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = CloudVersionController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            CloudVersionController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)

# create
class CloudVersionCreateView(TemplateView):
    template_name = 'cloud_version_controller/cloud_version_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = CloudVersionController()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)

# search
class CloudVersionSearchView(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'cloud_version_controller/cloud_version_search.html',
                          {'info': CloudVersionController.objects.get(name=request.GET.get('cloud_type_search'))})
        except Exception as e:
            print(e)
            return render(request, 'cloud_version_controller/cloud_version_list.html')

"""
产品管理
yibot/call 
"""

# list
class ProductTypeListView(ListView):
    template_name = 'business_products_controller/product_type_list.html'
    model = PcaProjectType
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(ProductTypeListView, self).get_context_data(**kwargs)
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

# update
class ProductTypeUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'business_products_controller/product_type_update.html',
                      {'product_type_obj': PcaProjectType.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            PcaProjectType.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                 updated_tm=datetime.datetime.now().strftime(
                                                                     '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)

# delete
class ProductTypeDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = PcaProjectType()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            PcaProjectType.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)

# create
class ProductTypeCreateView(TemplateView):
    template_name = 'business_products_controller/product_type_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = PcaProjectType()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)

# search
class ProductTypeSearchView(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'business_products_controller/product_type_search.html',
                          {'info': PcaProjectType.objects.get(name=request.GET.get('product_type_search'))})
        except Exception as e:
            print(e)
            return render(request, 'business_products_controller/product_type_list.html')


"""
环境类型
Proc/Test 
"""

# list
class ProductEnvTypeListView(ListView):
    template_name = 'product_env_type_controller/product_env_type_list.html'
    model = PcaProjectEnvController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(ProductEnvTypeListView, self).get_context_data(**kwargs)
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

# update
class ProductEnvTypeUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'product_env_type_controller/product_env_type_update.html',
                      {'product_type_obj': PcaProjectEnvController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            name = data.get('name')
            remark = data.get('remark')
            PcaProjectEnvController.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                 updated_tm=datetime.datetime.now().strftime(
                                                                     '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)

# delete
class ProductEnvTypeDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = PcaProjectEnvController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            PcaProjectEnvController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)

# create
class ProductEnvTypeCreateView(TemplateView):
    template_name = 'product_env_type_controller/product_env_type_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = PcaProjectEnvController()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)

# search
class ProductEnvTypeSearch(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'product_env_type_controller/product_env_type_search.html',
                          {'info': PcaProjectEnvController.objects.get(name=request.GET.get('product_type_search'))})
        except Exception as e:
            print(e)
            return render(request, 'product_env_type_controller/product_env_type_list.html')


"""
项目环境
"""
# list
class ProductEnvListView(ListView):
    template_name = 'product_env_controller/product_env_list.html'
    model = PcaProjectBelongController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(ProductEnvListView, self).get_context_data(**kwargs)
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

# update
class ProductEnvUpdateView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'product_env_controller/product_env_update.html',
                      {'project_type_obj': PcaProjectBelongController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        print(data)
        try:
            name = data.get('name')
            remark = data.get('remark')
            PcaProjectBelongController.objects.filter(id=data.get("id")).update(name=name, remark=remark,
                                                                  updated_tm=datetime.datetime.now().strftime(
                                                                      '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


class ProductEnvDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = PcaProjectBelongController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            PcaProjectBelongController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


class ProductEnvCreateView(TemplateView):
    template_name = 'product_env_controller/product_env_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            cloud = PcaProjectBelongController()
            cloud.name = data.get('name')
            cloud.remark = data.get('remark')
            cloud.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


class ProductEnvSearchView(View):
    def get(self, request):
        data = request.GET
        try:
            return render(request, 'product_env_controller/product_env_search.html',
                          {'info': PcaProjectBelongController.objects.get(name=request.GET.get('project_env_search'))})
        except Exception as e:
            print(e)
            return render(request, 'product_env_controller/product_env_list.html')
