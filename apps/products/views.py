from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator

from gsnky import settings
from products.models import ProductType, Product


class ProductsView(View):

    def get(self, request):
        product_type_nodes = ProductType.objects.all()
        product_list = Product.objects.all()

        # 关键字搜索
        key_words = request.GET.get('key_words', '')
        if key_words:
            product_list = product_list.filter(Q(name__icontains=key_words))

        # 左侧树类型查询
        level = request.GET.get('level', '')
        type_id = request.GET.get('typeid', '')
        if level:
            if int(level) == 0:
                product_list = Product.objects.select_related('type').filter(type__parent_id=int(type_id))
            elif int(level) == 1:
                if type_id:
                    product_list = product_list.filter(type_id=int(type_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(object_list=product_list, per_page=settings.Y_PAGING_ZB_NUM, request=request)
        product_list_paging = p.page(page)

        return render(request, 'zblist.html', {
            'nodes': product_type_nodes,
            'product_list': product_list_paging,
            'key_words': key_words,
        })
