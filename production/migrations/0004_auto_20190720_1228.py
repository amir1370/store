# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-20 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20190720_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='عکس'),
        ),
    ]