# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170917_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Заглавие')),
                ('under_title', models.CharField(default='', max_length=255, verbose_name='Текст под заглавием')),
                ('service_1_title', models.CharField(default='', max_length=255, verbose_name='Название услуги 1')),
                ('service_1_text', models.CharField(default='', max_length=255, verbose_name='Описание услуги 1')),
                ('service_1_icon', models.CharField(default='', max_length=255, verbose_name='Иконка услуги 1')),
                ('service_2_title', models.CharField(default='', max_length=255, verbose_name='Название услуги 2')),
                ('service_2_text', models.CharField(default='', max_length=255, verbose_name='Описание услуги 2')),
                ('service_2_icon', models.CharField(default='', max_length=255, verbose_name='Иконка услуги 2')),
                ('service_3_title', models.CharField(default='', max_length=255, verbose_name='Название услуги 3')),
                ('service_3_text', models.CharField(default='', max_length=255, verbose_name='Описание услуги 3')),
                ('service_3_icon', models.CharField(default='', max_length=255, verbose_name='Иконка услуги 3')),
            ],
            options={
                'verbose_name': 'Секция Services',
                'verbose_name_plural': 'Секция Services',
            },
        ),
    ]
