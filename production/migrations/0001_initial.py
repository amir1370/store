# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-05 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='نام دسته')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('up_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='production.Category')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='نام')),
                ('slug', models.SlugField(max_length=100, verbose_name='نام لاتین')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='عکس')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='production.Category', verbose_name='دسته')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
