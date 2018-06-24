from django.shortcuts import render
from django.views.generic.base import View

from zb.models import ZBList, GGZB, CDHJ


class ZBView(View):
    def get(self, request, product_id):
        list_ggzb_avg = []
        list_ggzb_range = []
        query_set_avg = GGZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=1)
        query_set_range = GGZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=2)
        for qs in query_set_avg:
            list_ggzb_avg.append(qs)
        for qs in query_set_range:
            list_ggzb_range.append(qs)
        return render(request, 'table.html', {
            'ggzb_avg': list_ggzb_avg,
            'ggzb_range': list_ggzb_range,
        })
