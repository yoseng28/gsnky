# Generated by Django 2.0.6 on 2018-06-23 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zb', '0003_auto_20180622_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zbvalue',
            name='zb_list',
            field=models.ForeignKey(limit_choices_to={'type': 'ggzb'}, on_delete=django.db.models.deletion.CASCADE, to='zb.ZBList', verbose_name='指标'),
        ),
    ]