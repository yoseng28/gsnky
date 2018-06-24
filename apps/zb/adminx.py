import xadmin

from .models import ZBList, ZBValue, CDHJ, GGZB, JBYYZB, TYXYYZB, DNATP


# 指标注册
class ZbAdmin(object):
    list_display = ['type', 'name']
    search_fields = ['type', 'name']
    list_filter = ['type', 'name']
    model_icon = 'fa fa-rocket'


class ZBValueAdmin(object):
    list_display = ['product', 'zb_list', 'value', 'avg_range']
    search_fields = ['product', 'zb_list', 'value', 'avg_range']
    list_filter = ['product', 'zb_list', 'value', 'avg_range']
    model_icon = 'fa fa-rocket'


class GGZBAdmin(object):
    list_display = ['product', 'zb_list', 'value', 'avg_range']
    search_fields = ['product', 'zb_list', 'value', 'avg_range']
    list_filter = ['product', 'zb_list', 'value', 'avg_range']
    model_icon = 'fa fa-rocket'


class JBYYZBAdmin(object):
    list_display = ['product', 'zb_list', 'value', 'avg_range']
    search_fields = ['product', 'zb_list', 'value', 'avg_range']
    list_filter = ['product', 'zb_list', 'value', 'avg_range']
    model_icon = 'fa fa-rocket'


class TYXYYZBAdmin(object):
    list_display = ['product', 'zb_list', 'value', 'avg_range']
    search_fields = ['product', 'zb_list', 'value', 'avg_range']
    list_filter = ['product', 'zb_list', 'value', 'avg_range']
    model_icon = 'fa fa-rocket'


class DNATPAdmin(object):
    list_display = ['product', 'zb_list', 'value', 'avg_range']
    search_fields = ['product', 'zb_list', 'value', 'avg_range']
    list_filter = ['product', 'zb_list', 'value', 'avg_range']
    model_icon = 'fa fa-rocket'


class CDHJAdmin(object):
    list_display = ['product', 'zb_list', 'value', 'avg_range']
    search_fields = ['product', 'zb_list', 'value', 'avg_range']
    list_filter = ['product', 'zb_list', 'value', 'avg_range']
    model_icon = 'fa fa-rocket'


xadmin.site.register(ZBList, ZbAdmin)
xadmin.site.register(ZBValue, ZBValueAdmin)
xadmin.site.register(GGZB, GGZBAdmin)
xadmin.site.register(JBYYZB, JBYYZBAdmin)
xadmin.site.register(TYXYYZB, TYXYYZBAdmin)
xadmin.site.register(DNATP, DNATPAdmin)
xadmin.site.register(CDHJ, CDHJAdmin)
