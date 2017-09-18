# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_headercontactssection'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('description', models.CharField(default='', max_length=255, verbose_name='Description')),
                ('keywords', models.CharField(default='', max_length=255, verbose_name='keywords')),
            ],
            options={
                'verbose_name': 'Настройки SEO (метатеги)',
                'verbose_name_plural': 'Настройки SEO (метатеги)',
            },
        ),
    ]