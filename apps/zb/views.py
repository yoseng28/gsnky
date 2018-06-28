from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.generic.base import View

from gsnky import settings
from products.models import Product
from zb.models import GGZB, CDHJ, JBYYZB, DNATP, TYXYYZB


class ZBView(View):
    def get(self, request, product_id):

        # 未登录跳转login
        if not request.user.is_authenticated:
            return redirect('/login/?next=/zblist/')

        # 产品不存在
        product_ = Product.objects.get(id=product_id)
        if product_ is None:
            return render(request, 'zbinfo.html', {})

        ggzb_range = []
        jbyyzb_range = [],
        tyxyyzb_range = [],
        dnatp_range = [],
        cdhj_range = [],

        flag = False
        try:
            groups_list = request.user.groups.all()
            for g in groups_list:
                if g.name == settings.Y_GROUP_ZJ:
                    flag = True
        except Group.DoesNotExist:
            pass

        # 专家用户显示范围值
        if flag:
            ggzb_range, jbyyzb_range, tyxyyzb_range, dnatp_range, cdhj_range = ZBView.query_zb(self, product_id, 2)

        ggzb_avg, jbyyzb_avg, tyxyyzb_avg, dnatp_avg, cdhj_avg = ZBView.query_zb(self, product_id, 1)

        return render(request, 'zbinfo.html', {
            'product_name': product_.name,
            # 平均值
            'ggzb_avg': ggzb_avg,
            'jbyyzb_avg': jbyyzb_avg,
            'tyxyyzb_avg': tyxyyzb_avg,
            'dnatp_avg': dnatp_avg,
            'cdhj_avg': cdhj_avg,
            # 范围
            'ggzb_range': ggzb_range,
            'jbyyzb_range': jbyyzb_range,
            'tyxyyzb_range': tyxyyzb_range,
            'dnatp_range': dnatp_range,
            'cdhj_range': cdhj_range,
        })

    # 指标查询 1平均值2范围
    def query_zb(self, product_id, avg_range):
        query_ggzb = GGZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=avg_range) \
            .order_by('zb_list_id')
        query_jbyyzb = JBYYZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=avg_range) \
            .order_by('zb_list_id')
        query_tyxyyzb = TYXYYZB.objects.select_related('zb_list').filter(product_id=product_id, avg_range=avg_range) \
            .order_by('zb_list_id')
        query_dnatp = DNATP.objects.select_related('zb_list').filter(product_id=product_id, avg_range=avg_range) \
            .order_by('zb_list_id')
        query_cdhj = CDHJ.objects.select_related('zb_list').filter(product_id=product_id, avg_range=avg_range) \
            .order_by('zb_list_id')

        ggzb = ZBView.build_list_zb(query_ggzb)
        jbyyzb = ZBView.build_list_zb(query_jbyyzb)
        tyxyyzb = ZBView.build_list_zb(query_tyxyyzb)
        dnatp = ZBView.build_list_zb(query_dnatp)
        cdhj = ZBView.build_list_zb(query_cdhj)

        return ggzb, jbyyzb, tyxyyzb, dnatp, cdhj

    @staticmethod
    def build_list_zb(query_set_zb):
        temp = []
        for qs in query_set_zb:
            temp.append(qs)
        return temp
