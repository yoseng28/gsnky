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

from commodity.views import CommodityListView, CommodityInfoView
from gsnky.settings import MEDIA_ROOT
from information.views import InformationListView, InformationView
from products.views import ProductsView
from users.views import LoginView, RegisterView, LogoutView
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

    # 指标
    path('zblist/', ProductsView.as_view(), name='zblist'),
    re_path(r'^zbinfo/(?P<product_id>.*)/$', ZBView.as_view(), name='zb_view'),
    # 商品展示
    path('comlist/', CommodityListView.as_view(), name='comlist'),
    re_path(r'^cominfo/(?P<commodity_id>.*)/$', CommodityInfoView.as_view(), name='cominfo'),
    # 新闻通告
    path('infolist/', InformationListView.as_view(), name='infolist'),
    path('info/', InformationView.as_view(), name='info'),

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')


]
