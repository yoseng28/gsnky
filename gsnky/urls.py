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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve

from gsnky.settings import MEDIA_ROOT
from products.views import productsTreeView
from zb.views import ZBView

urlpatterns = [
    path('admin/', xadmin.site.urls),

    # 上传文件的访问配置
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # Plugins
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 静态页面跳转
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('baidumap/', TemplateView.as_view(template_name='map.html'), name='baidumap'),

    # 指标树显示
    path('zblist/', productsTreeView, name='zblist'),
    # 指标详情页
    re_path(r'^zblist/(?P<product_id>.*)/$', ZBView.as_view(), name='zb_view'),

]
