from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator

from gsnky import settings
from information.models import Information, InformationType


class InformationView(View):

    def get(self, request):
        id_ = request.GET.get('id', '')
        info = Information.objects.get(id=id_)
        return render(request, 'info.html', {
            'info': info
        })


class InformationListView(View):

    def get(self, request):
        info_type = InformationType.objects.all()
        info_list = Information.objects.all()

        # 关键字搜索
        key_words = request.GET.get('key_words', '')
        if key_words:
            info_list = info_list.filter(Q(name__icontains=key_words))

        # 左侧树类型查询
        type_id = request.GET.get('typeid', '')
        if type_id:
            info_list = info_list.filter(type_id=int(type_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(object_list=info_list, per_page=settings.Y_PAGING_INFO_NUM, request=request)
        info_list_paging = p.page(page)

        return render(request, 'infolist.html', {
            'info_type': info_type,
            'info_list': info_list_paging,
            'key_words': key_words,
            'type_id': type_id,
        })
