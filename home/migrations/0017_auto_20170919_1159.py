# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_seosettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesection',
            name='text_6',
            field=models.CharField(default='', max_length=255, verbose_name='Текст 6'),
        ),
        migrations.AlterField(
            model_name='homesection',
            name='text_4',
            field=models.TextField(default='', verbose_name='Текст 4'),
        ),
    ]