from django.db import models

from products.models import Product


class ZBList(models.Model):
    name = models.CharField(max_length=50, verbose_name='指标名称')
    type = models.CharField(max_length=20, default='ggzb', verbose_name='指标类型',
                            choices=(('ggzb', '感官指标'),
                                     ('jbyy', '基本营养指标'),
                                     ('tyxyy', '特异性营养指标'),
                                     ('dnatp', 'DNA图谱'),
                                     ('cdhj', '产地环境')))
    info = models.CharField(max_length=200, verbose_name='指标描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_list'
        verbose_name = '新增指标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ZBValue(models.Model):
    value = models.CharField(max_length=50, verbose_name='指标值')
    avg_range = models.IntegerField(default=1, verbose_name='平均-范围',
                                    choices=((1, '平均值'), (2, '范围')))
    product = models.ForeignKey(Product, '产品', verbose_name='产品')
    zb_list = models.ForeignKey(ZBList, verbose_name='指标', on_delete=models.CASCADE,
                                limit_choices_to={'type': 'ggzb'}
                                )
    info = models.CharField(max_length=200, verbose_name='指标值描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_value'
        verbose_name = '指标值'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


# 感官指标
class GGZB(models.Model):
    value = models.CharField(max_length=50, verbose_name='指标值')
    avg_range = models.IntegerField(default=1, verbose_name='平均-范围',
                                    choices=((1, '平均值'), (2, '范围')))
    product = models.ForeignKey(Product, '产品', verbose_name='产品')
    zb_list = models.ForeignKey(ZBList, verbose_name='指标',
                                on_delete=models.CASCADE,
                                limit_choices_to={'type': 'ggzb'})
    info = models.CharField(max_length=200, verbose_name='指标值描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_gg'
        verbose_name = '感官指标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


# 基本营养指标
class JBYYZB(models.Model):
    value = models.CharField(max_length=50, verbose_name='指标值')
    avg_range = models.IntegerField(default=1, verbose_name='平均-范围',
                                    choices=((1, '平均值'), (2, '范围')))
    product = models.ForeignKey(Product, '产品', verbose_name='产品')
    zb_list = models.ForeignKey(ZBList, verbose_name='指标', on_delete=models.CASCADE,
                                limit_choices_to={'type': 'jbyy'})
    info = models.CharField(max_length=200, verbose_name='指标值描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_jbyy'
        verbose_name = '基本营养指标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


# 特异性营养指标
class TYXYYZB(models.Model):
    value = models.CharField(max_length=50, verbose_name='指标值')
    avg_range = models.IntegerField(default=1, verbose_name='平均-范围',
                                    choices=((1, '平均值'), (2, '范围')))
    product = models.ForeignKey(Product, '产品', verbose_name='产品')
    zb_list = models.ForeignKey(ZBList, verbose_name='指标',
                                on_delete=models.CASCADE,
                                limit_choices_to={'type': 'tyxyy'})
    info = models.CharField(max_length=200, verbose_name='指标值描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_tyxyy'
        verbose_name = '特异性营养指标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


# DNA图谱
class DNATP(models.Model):
    value = models.CharField(max_length=50, verbose_name='指标值')
    avg_range = models.IntegerField(default=1, verbose_name='平均-范围',
                                    choices=((1, '平均值'), (2, '范围')))
    product = models.ForeignKey(Product, '产品', verbose_name='产品')
    zb_list = models.ForeignKey(ZBList, verbose_name='指标',
                                on_delete=models.CASCADE,
                                limit_choices_to={'type': 'dnatp'})
    info = models.CharField(max_length=200, verbose_name='指标值描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_dnatp'
        verbose_name = 'DNA图谱'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


# 产地环境
class CDHJ(models.Model):
    value = models.CharField(max_length=50, verbose_name='指标值')
    avg_range = models.IntegerField(default=1, verbose_name='平均-范围',
                                    choices=((1, '平均值'), (2, '范围')))
    product = models.ForeignKey(Product, '产品', verbose_name='产品')
    zb_list = models.ForeignKey(ZBList, verbose_name='指标', on_delete=models.CASCADE,
                                limit_choices_to={'type': 'cdhj'}
                                )
    info = models.CharField(max_length=200, verbose_name='指标值描述', null=True, blank=True)

    class Meta:
        db_table = 'zb_cdhj'
        verbose_name = '产地环境'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value
