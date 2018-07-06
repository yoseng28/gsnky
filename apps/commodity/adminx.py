import xadmin

from commodity.models import Commodity, CommodityType


class CommodityAdmin(object):

    def get_readonly_fields(self):
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('add_time',)
    list_display = ['name', 'type', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'type', 'add_time']
    model_icon = 'fa fa-certificate'
    style_fields = {"detail": "ueditor"}


class CommodityTypeAdmin(object):

    def get_readonly_fields(self):
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('add_time',)
    list_display = ['name', 'parent', 'get_commodity_num']
    search_fields = ['name']
    model_icon = 'fa fa-certificate'


xadmin.site.register(Commodity, CommodityAdmin)
xadmin.site.register(CommodityType, CommodityTypeAdmin)
