from django.views.generic import TemplateView
from . import models
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate


class IndexView(TemplateView):
    template_name = 'index/index.html'


class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        data = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            res = {'status': 0, 'msg': '登陆成功'}
        else:
            res = {'status': 1, 'msg': '用户密码错误'}

        return JsonResponse(res)
