from django.db import models
from django.conf import settings


class HomeSection(models.Model):
    """Модель для секции Home."""
    text_1 = models.CharField(verbose_name='Текст 1', default='', max_length=255)
    text_2 = models.CharField(verbose_name='Текст 2 (тег h1)', default='', max_length=255)
    text_3 = models.CharField(verbose_name='Текст 3', default='', max_length=255)
    text_4 = models.CharField(verbose_name='Текст 4', default='', max_length=255)
    text_5 = models.CharField(verbose_name='Текст 5', default='', max_length=255)

    def __str__(self):
        return 'Секция Home'

    class Meta:
        verbose_name = 'Секция Home'
        verbose_name_plural = 'Секция Home'


class AboutSection(models.Model):
    """Модель для секции About."""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)
    text = models.TextField(verbose_name='Текст', default='')
    image_1 = models.ImageField(verbose_name='Изображение 1', upload_to='uploads/')
    image_2 = models.ImageField(verbose_name='Изображение 2', upload_to='uploads/')
    image_3 = models.ImageField(verbose_name='Изображение 3', upload_to='uploads/')

    def __str__(self):
        return 'Секция About'

    class Meta:
        verbose_name = 'Секция About'
        verbose_name_plural = 'Секция About'
