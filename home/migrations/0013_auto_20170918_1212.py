# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_testimonialssection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialssection',
            name='item_1_name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя клиента 1'),
        ),
        migrations.AlterField(
            model_name='testimonialssection',
            name='item_1_position',
            field=models.CharField(default='', max_length=255, verbose_name='Должность клиента 1'),
        ),
        migrations.AlterField(
            model_name='testimonialssection',
            name='item_2_name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя клиента 2'),
        ),
        migrations.AlterField(
            model_name='testimonialssection',
            name='item_2_position',
            field=models.CharField(default='', max_length=255, verbose_name='Должность клиента 2'),
        ),
        migrations.AlterField(
            model_name='testimonialssection',
            name='item_3_name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя клиента 3'),
        ),
        migrations.AlterField(
            model_name='testimonialssection',
            name='item_3_position',
            field=models.CharField(default='', max_length=255, verbose_name='Должность клиента 3'),
        ),
    ]
