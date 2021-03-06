# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170917_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Заглавие')),
                ('under_title', models.CharField(default='', max_length=255, verbose_name='Текст под заглавием')),
                ('skill_1_title', models.CharField(default='', max_length=255, verbose_name='Название принципа 1')),
                ('skill_1_value', models.IntegerField(default='', max_length=255, verbose_name='Значение принципа 1')),
                ('skill_2_title', models.CharField(default='', max_length=255, verbose_name='Название принципа 2')),
                ('skill_2_value', models.IntegerField(default='', max_length=255, verbose_name='Значение принципа 2')),
                ('skill_3_title', models.CharField(default='', max_length=255, verbose_name='Название принципа 3')),
                ('skill_3_value', models.IntegerField(default='', max_length=255, verbose_name='Значение принципа 3')),
            ],
            options={
                'verbose_name': 'Секция Skills',
                'verbose_name_plural': 'Секция Skills',
            },
        ),
    ]
