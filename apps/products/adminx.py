import xadmin
from .models import Product, ProductType


class ProductsAdmin(object):
    list_display = ['name', 'type']
    search_fields = ['name']
    list_filter = ['name', 'type']
    model_icon = 'fa fa-file-text'


class ProductsTypeAdmin(object):
    list_display = ['name', 'parent']
    search_fields = ['name']
    list_filter = ['name', 'parent']
    model_icon = 'fa fa-file-text'


xadmin.site.register(Product, ProductsAdmin)
xadmin.site.register(ProductType, ProductsTypeAdmin)
