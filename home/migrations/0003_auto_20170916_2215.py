# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170916_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='image_1',
            field=models.ImageField(upload_to='D:\\python_projects\\priem-metall\\static/assets/images/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='aboutsection',
            name='image_2',
            field=models.ImageField(upload_to='D:\\python_projects\\priem-metall\\static/assets/images/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='aboutsection',
            name='image_3',
            field=models.ImageField(upload_to='D:\\python_projects\\priem-metall\\staticmak/assets/images/', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='aboutsection',
            name='text',
            field=models.TextField(default='', verbose_name='Текст'),
        ),
    ]