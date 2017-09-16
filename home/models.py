from django.db import models


class HomeSection(models.Model):
    """Модель для секции Home."""
    text_1 = models.CharField(verbose_name='Текст 1', default='', max_length=255)
    text_2 = models.CharField(verbose_name='Текст 2 (тег h1)', default='', max_length=255)
    text_3 = models.CharField(verbose_name='Текст 3', default='', max_length=255)
    text_4 = models.CharField(verbose_name='Текст 4', default='', max_length=255)
    text_5 = models.CharField(verbose_name='Текст 5', default='', max_length=255)

    class Meta:
        verbose_name = 'Секция Home'
        verbose_name_plural = 'Секция Home'
