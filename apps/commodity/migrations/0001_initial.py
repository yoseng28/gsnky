# Generated by Django 2.0.6 on 2018-06-26 13:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import extra_apps.DjangoUeditor.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('carousel_pic', models.ImageField(blank=True, null=True, upload_to='goods/carousel/', verbose_name='上传首页轮播器图片')),
                ('info', models.CharField(blank=True, max_length=500, null=True, verbose_name='商品描述')),
                ('detail', extra_apps.DjangoUeditor.models.UEditorField(default='', verbose_name='商品详情')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'Commodity',
            },
        ),
        migrations.CreateModel(
            name='CommodityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='商品类型名称')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='commodity.CommodityType', verbose_name='上一级')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
                'db_table': 'commodity_type',
            },
        ),
        migrations.AddField(
            model_name='commodity',
            name='type',
            field=models.ForeignKey(limit_choices_to={'level': 1}, on_delete=django.db.models.deletion.CASCADE, to='commodity.CommodityType', verbose_name='商品类型'),
        ),
    ]