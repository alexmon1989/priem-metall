# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20170922_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobschemesection',
            name='under_text',
            field=models.TextField(default='', verbose_name='Текст внизу секции'),
        ),
        migrations.AlterField(
            model_name='whyussection',
            name='under_text',
            field=models.TextField(default='', verbose_name='Текст внизу секции'),
        ),
    ]
