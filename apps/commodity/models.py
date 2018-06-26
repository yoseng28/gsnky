from datetime import datetime

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from extra_apps.DjangoUeditor.models import UEditorField


class CommodityType(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='商品类型名称')
    parent = TreeForeignKey('self', verbose_name='上一级', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'commodity_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Commodity(models.Model):
    name = models.CharField(max_length=50, verbose_name='商品名称')
    type = models.ForeignKey(CommodityType, verbose_name='商品类型',
                             on_delete=models.CASCADE,
                             limit_choices_to={'level': 1})
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    pic = models.ImageField(verbose_name='上传商品展示图片',
                            null=True, blank=True,
                            upload_to='goods/')
    info = models.CharField(max_length=500, verbose_name='商品描述', null=True, blank=True)
    detail = UEditorField(verbose_name="商品详情",
                          width=800, height=1024,
                          toolbars='full',
                          upload_settings={'imageMaxSize': 4204000},
                          imagePath="goods/ueditor/",
                          filePath="goods/ueditor/",
                          default='')

    class Meta:
        db_table = 'Commodity'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
