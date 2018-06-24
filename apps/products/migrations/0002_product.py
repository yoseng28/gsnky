# Generated by Django 2.0.6 on 2018-06-22 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品名称')),
                ('info', models.CharField(blank=True, max_length=500, null=True, verbose_name='产品概述')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductType', verbose_name='产品类型')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'db_table': 'product',
            },
        ),
    ]