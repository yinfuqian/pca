# Create your views here.
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, request, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import *

"""
用户管理
"""


# 用户显示
class UserListView(ListView):
    template_name = 'account/user_list.html'
    model = PcaUserController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['page_range'] = self.page_range(context['page_obj'], context['paginator'])
        # print(context)
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


# 用户搜索
class UserSearch(View):
    def get(self, request):
        data = request.GET
        print(request.GET.get('user_name'))
        try:
            return render(request, 'account/user_search.html',
                          {'info': PcaUserController.objects.get(username=request.GET.get('user_name'))})
        except Exception as e:
            print(e)
            return render(request, 'account/user_list.html')


# 添加用户
class UserAddView(TemplateView):
    template_name = 'account/user_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            user = PcaUserController()
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.phone = data.get('phone')
            user.is_active = data.get('is_act')
            user.is_superuser = data.get('is_sup')
            user.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# 删除用户
class UserDeleteView(View):
    def get(self, request):
        data = request.GET
        user = PcaUserController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            PcaUserController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


# 更新用户
class UserUpdateView(View):

    def get(self, request):
        data = request.GET
        # print(PcaUserController.objects.get(id=request.GET.get('id')))
        return render(request, 'account/user_edit.html',
                      {'user_obj': PcaUserController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        print(data)
        res = {'status': 0, 'msg': '更新成功'}
        try:
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            phone = data.get('phone')
            is_active = data.get('is_act')
            is_superuser = data.get('is_sup')
            role = data.get('account')
            PcaUserController.objects.filter(id=data.get("id")).update(username=username, email=email, phone=phone,
                                                                       is_active=is_active, is_superuser=is_superuser,
                                                                       role=role)

        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# 状态更新
class UserStatus(View):
    def get(self, request):
        data = request.GET

        res = {'status': 0}

        user = PcaUserController.objects.get(id=data.get('id'))
        status = user.is_active

        if status == 0:
            new_status = 1
        else:
            new_status = 0
        try:
            user = PcaUserController.objects.get(id=data.get('id'))
            user.is_active = new_status
            user.save()
        except Exception as e:
            print(e)
            res = {'status': 1}
        return JsonResponse(res)


# SSH用户展示
class SSHListView(View):
    def get(self, request):
        ret = PcaSshUserController.objects.all().order_by('id')
        print(ret)
        return render(request, 'account/ssh_user_list.html',
                      {'users': ret})
