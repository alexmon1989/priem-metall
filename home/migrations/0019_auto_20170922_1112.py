# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20170919_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicessection',
            name='service_1_text',
            field=models.TextField(default='', verbose_name='Описание услуги 1'),
        ),
        migrations.AlterField(
            model_name='servicessection',
            name='service_2_text',
            field=models.TextField(default='', verbose_name='Описание услуги 2'),
        ),
        migrations.AlterField(
            model_name='servicessection',
            name='service_3_text',
            field=models.TextField(default='', verbose_name='Описание услуги 3'),
        ),
        migrations.AlterField(
            model_name='servicessection',
            name='service_4_text',
            field=models.TextField(default='', verbose_name='Описание услуги 4'),
        ),
    ]
