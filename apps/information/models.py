from datetime import datetime

from django.db import models

from extra_apps.DjangoUeditor.models import UEditorField


class InformationType(models.Model):
    name = models.CharField(max_length=50, verbose_name='信息类型')
    info = models.CharField(max_length=500, verbose_name='信息类型描述', null=True, blank=True)

    class Meta:
        db_table = 'information_type'
        verbose_name = '信息类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Information(models.Model):
    publisher = models.CharField(max_length=50, verbose_name='信息名称', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='信息名称')
    type = models.ForeignKey(InformationType, verbose_name='信息类型',
                             on_delete=models.CASCADE, )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    pic = models.ImageField(verbose_name='上传展示图片',
                            null=True, blank=True,
                            upload_to='information/')
    info = models.CharField(max_length=500, verbose_name='信息描述', null=True, blank=True)
    detail = UEditorField(verbose_name="信息详情",
                          width=800, height=1024,
                          toolbars='full',
                          upload_settings={'imageMaxSize': 4204000},
                          imagePath="information/ueditor/",
                          filePath="information/ueditor/",
                          default='')

    class Meta:
        db_table = 'information'
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
