from django.shortcuts import render
from django.views.generic.base import View

from products.models import Product
from zb.models import GGZB, CDHJ, JBYYZB, DNATP, TYXYYZB


class ZBView(View):
    def get(self, request, product_id):

        product_ = Product.objects.get(id=product_id)
        if product_ is None:
            return render(request, 'zbinfo.html', {})

        # 指标-平均值
        query_ggzb_avg = GGZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=1) \
            .order_by('zb_list_id')
        query_jbyyzb_avg = JBYYZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=1) \
            .order_by('zb_list_id')
        query_tyxyyzb_avg = TYXYYZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=1) \
            .order_by('zb_list_id')
        query_dnatp_avg = DNATP.objects.select_related('zb_list').filter(product_id=product_id, avg_range=1) \
            .order_by('zb_list_id')
        query_cdhj_avg = CDHJ.objects.select_related('zb_list').filter(product_id=product_id, avg_range=1) \
            .order_by('zb_list_id')

        # 指标-范围
        query_ggzb_range = GGZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=2) \
            .order_by('zb_list_id')
        query_jbyyzb_range = JBYYZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=2) \
            .order_by('zb_list_id')
        query_tyxyyzb_range = TYXYYZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=2) \
            .order_by('zb_list_id')
        query_dnatp_range = DNATP.objects.select_related('zb_list').filter(product_id=product_id, avg_range=2) \
            .order_by('zb_list_id')
        query_cdhj_range = CDHJ.objects.select_related('zb_list').filter(product_id=product_id, avg_range=2) \
            .order_by('zb_list_id')

        return render(request, 'zbinfo.html', {
            'product_name': product_.name,
            # 平均值
            'ggzb_avg': ZBView.build_list_zb(query_ggzb_avg),
            'jbyyzb_avg': ZBView.build_list_zb(query_jbyyzb_avg),
            'tyxyyzb_avg': ZBView.build_list_zb(query_tyxyyzb_avg),
            'dnatp_avg': ZBView.build_list_zb(query_dnatp_avg),
            'cdhj_avg': ZBView.build_list_zb(query_cdhj_avg),
            # 范围
            'ggzb_range': ZBView.build_list_zb(query_ggzb_range),
            'jbyyzb_range': ZBView.build_list_zb(query_jbyyzb_range),
            'tyxyyzb_range': ZBView.build_list_zb(query_tyxyyzb_range),
            'dnatp_range': ZBView.build_list_zb(query_dnatp_range),
            'cdhj_range': ZBView.build_list_zb(query_cdhj_range),
        })

    @staticmethod
    def build_list_zb(query_set_zb):
        temp = []
        for qs in query_set_zb:
            temp.append(qs)
        return temp
