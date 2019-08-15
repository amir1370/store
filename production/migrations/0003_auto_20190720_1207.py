# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-20 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20190705_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d', verbose_name='عکس'),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.FloatField(blank=True, null=True, verbose_name='طول'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='سایز'),
        ),
        migrations.AddField(
            model_name='product',
            name='thickness',
            field=models.FloatField(blank=True, null=True, verbose_name='ضخامت'),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.FloatField(blank=True, null=True, verbose_name='عرض'),
        ),
    ]
