# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Заглавие')),
                ('under_title', models.CharField(default='', max_length=255, verbose_name='Текст под заглавием')),
                ('text', models.TextField(default='', max_length=255, verbose_name='Текст')),
                ('image_1', models.ImageField(upload_to='static/assets/images/', verbose_name='Изображение 1')),
                ('image_2', models.ImageField(upload_to='static/assets/images/', verbose_name='Изображение 2')),
                ('image_3', models.ImageField(upload_to='static/assets/images/', verbose_name='Изображение 3')),
            ],
            options={
                'verbose_name_plural': 'Секция About',
                'verbose_name': 'Секция About',
            },
        ),
        migrations.AlterModelOptions(
            name='homesection',
            options={'verbose_name': 'Секция Home', 'verbose_name_plural': 'Секция Home'},
        ),
        migrations.AlterField(
            model_name='homesection',
            name='text_2',
            field=models.CharField(default='', max_length=255, verbose_name='Текст 2 (тег h1)'),
        ),
    ]
