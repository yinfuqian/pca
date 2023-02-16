"""pca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^dashboard/', include('dashboard.urls')),
    re_path(r'^$', RedirectView.as_view(url='/login/')),
    re_path(r'login/', LoginView.as_view(), name='user_login'),
    re_path(r'index/', IndexView.as_view(), name='index'),
    re_path(r'users/', include('pca_system_controller.urls')),
    re_path(r'pca_cloud_capitals/', include('pca_cloud_capitals.urls')),
    re_path(r'pca_static_capitals/', include('pca_static_capitals.urls')),
    re_path(r'pca_business_controller/', include('pca_business_controller.urls')),
    re_path(r'api/', include('api.urls'))
]
