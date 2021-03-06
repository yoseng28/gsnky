# Generated by Django 2.0.6 on 2018-06-26 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180622_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(limit_choices_to={'level': 1}, on_delete=django.db.models.deletion.CASCADE, to='products.ProductType', verbose_name='产品类型'),
        ),
    ]
