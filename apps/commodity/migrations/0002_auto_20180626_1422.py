# Generated by Django 2.0.6 on 2018-06-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='carousel_pic',
        ),
        migrations.AddField(
            model_name='commodity',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='goods/', verbose_name='上传商品展示图片'),
        ),
    ]
