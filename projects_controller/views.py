import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import ProjectsController

# Create your views here.
"""
项目相关
列表/创建/删除/更新/搜索
"""


# list
class ProjectsControllerListView(ListView):
    template_name = 'projects_controller/projects_controller_list.html'
    model = ProjectsController
    ordering = 'id'
    paginate_by = 8  # 单页显示

    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')

    def get_context_data(self, **kwargs):
        context = super(ProjectsControllerListView, self).get_context_data(**kwargs)
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
class ProjectsControllerUpdataView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'projects_controller/projects_controller_update.html',
                      {'project_obj': ProjectsController.objects.get(id=request.GET.get('id'))})

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '更新成功'}
        try:
            projects = ProjectsController()
            name = data.get('name')
            project_type = data.get('project_type')
            products_name = data.get('products_name')
            products_install_type = data.get('products_install_type')
            t_remark = data.get('t_remark')
            m_remark = data.get('m_remark')
            p_remark = data.get('p_remark')
            remark = data.get('remark')
            print(t_remark)
            ProjectsController.objects.filter(id=data.get("id")).update(name=name, project_type=project_type,
                                                                        products_name=products_name,
                                                                        products_install_type=products_install_type,
                                                                        t_remark=t_remark, m_remark=m_remark,
                                                                        p_remark=p_remark, remark=remark,
                                                                        updated_tm=datetime.datetime.now().strftime(
                                                                            '%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '更新失败'}
        return JsonResponse(res)


# delete
class ProjectsControllerDeleteView(View):
    def get(self, request):
        data = request.GET
        cloud = ProjectsController()
        res = {'status': 0, 'msg': '删除成功'}
        try:
            ProjectsController.objects.get(id=data.get('id')).delete()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '删除失败'}
        return JsonResponse(res)


# create
class ProjectsControllerCreateView(TemplateView):
    template_name = 'projects_controller/projects_controller_create.html'

    def post(self, request):
        data = request.POST
        res = {'status': 0, 'msg': '添加成功'}
        try:
            projects = ProjectsController()
            projects.name = data.get('name')
            projects.project_type = data.get('project_type')
            projects.products_name = data.get('products_name')
            projects.products_install_type = data.get('products_install_type')
            projects.remark = data.get('remark')
            projects.t_remark = data.get('t_remark')
            projects.m_remark = data.get('m_remark')
            projects.p_remark = data.get('p_remark')
            projects.save()
        except Exception as e:
            print(e)
            res = {'status': '1', 'msg': '添加失败'}
        return JsonResponse(res)


# search

class ProjectsControllerSearchView(View):
    def get(self, request):
        data = request.GET
        print(data)
        try:
            if data.get('cloud_servers_search') == "":
                return render(request, 'projects_controller/projects_controller_search.html', {
                    'info': ProjectsController.objects.get(
                        project_type=request.GET.get('project_type'))})
            else:
                return render(request, 'projects_controller/projects_controller_search.html', {
                    'info': ProjectsController.objects.get(
                        name=request.GET.get('project_controller_search'))})
        except Exception as e:
            print(e)
            return render(request, 'projects_controller/projects_controller_list.html')


# more
class ProjectsControllerMoreView(View):

    def get(self, request):
        data = ProjectsController.objects.filter(id=request.GET.get('id'))
        print(data)
        return render(request, 'projects_controller/projects_controller_more.html', {'data': data})

