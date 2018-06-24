"""gsnky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import xadmin
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve

from gsnky.settings import MEDIA_ROOT
from zb.views import ZBView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', xadmin.site.urls),
    # 上传文件的访问配置
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    re_path(r'^zb/(?P<product_id>.*)/$', ZBView.as_view(), name='zb_view'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]
