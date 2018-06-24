from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class ProductType(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='产品类型名称')
    parent = TreeForeignKey('self', verbose_name='上一级', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # class MPTTMeta:
    #     order_insertion_by = ['name']

    class Meta:
        db_table = 'product_type'
        verbose_name = '产品类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='产品名称')
    info = models.CharField(max_length=500, verbose_name='产品概述', null=True, blank=True)
    type = models.ForeignKey(ProductType,
                             verbose_name='产品类型',
                             on_delete=models.CASCADE,
                             limit_choices_to={'level': 1})

    class Meta:
        db_table = 'product'
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
