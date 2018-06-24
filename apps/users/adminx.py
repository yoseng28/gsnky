import xadmin
from xadmin import views
# from extra_apps import xadmin
# from extra_apps.xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '农科院后台管理系统'
    site_footer = '版权所有@农科院'
    menu_style = 'accordion'


class ListSetting(object):
    list_per_page = 10


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.ListAdminView, ListSetting)
