# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-01 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_auto_20190726_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='رنگ'),
        ),
    ]