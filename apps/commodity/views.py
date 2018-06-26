from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator

from commodity.models import CommodityType, Commodity
from gsnky import settings


class CommodityInfoView(View):
    def get(self, request, commodity_id):
        commodity_ = Commodity.objects.get(id=commodity_id)
        return render(request, 'cominfo.html', {
            'commodity': commodity_
        })


class CommodityListView(View):

    def get(self, request):
        commodity_type_nodes = CommodityType.objects.all()
        commodity_list = Commodity.objects.all()

        # 关键字搜索
        key_words = request.GET.get('key_words', '')
        if key_words:
            commodity_list = commodity_list.filter(Q(name__icontains=key_words))

        # 左侧树类型查询
        level = request.GET.get('level', '')
        type_id = request.GET.get('typeid', '')
        if level:
            if int(level) == 0:
                commodity_list = Commodity.objects.select_related('type').filter(type__parent_id=int(type_id))
            elif int(level) == 1:
                if type_id:
                    commodity_list = commodity_list.filter(type_id=int(type_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(object_list=commodity_list, per_page=settings.Y_PAGING_COMMODITY_NUM, request=request)
        commodity_list_paging = p.page(page)

        return render(request, 'comlist.html', {
            'nodes': commodity_type_nodes,
            'commodity_list': commodity_list_paging,
            'key_words': key_words,
        })
