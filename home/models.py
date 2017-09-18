from django.db import models


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


class FactsSection(models.Model):
    """Модель для секции Facts"""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)

    fact_1_title = models.CharField(verbose_name='Название факта 1', default='', max_length=255)
    fact_1_value = models.IntegerField(verbose_name='Значение факта 1', default=0)
    fact_1_icon = models.CharField(verbose_name='Иконка факта 1', default='', max_length=255)

    fact_2_title = models.CharField(verbose_name='Название факта 2', default='', max_length=255)
    fact_2_value = models.IntegerField(verbose_name='Значение факта 2', default=0)
    fact_2_icon = models.CharField(verbose_name='Иконка факта 2', default='', max_length=255)

    fact_3_title = models.CharField(verbose_name='Название факта 3', default='', max_length=255)
    fact_3_value = models.IntegerField(verbose_name='Значение факта 3', default=0)
    fact_3_icon = models.CharField(verbose_name='Иконка факта 3', default='', max_length=255)

    def __str__(self):
        return 'Секция Facts'

    class Meta:
        verbose_name = 'Секция Facts'
        verbose_name_plural = 'Секция Facts'


class WhyUsSection(models.Model):
    """Модель для секции WhyUs"""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)

    reason_1_title = models.CharField(verbose_name='Название причины 1', default='', max_length=255)
    reason_1_text = models.CharField(verbose_name='Текст причины 1', default='', max_length=255)
    reason_1_icon = models.CharField(verbose_name='Иконка причины 1', default='', max_length=255)

    reason_2_title = models.CharField(verbose_name='Название причины 2', default='', max_length=255)
    reason_2_text = models.CharField(verbose_name='Текст причины 2', default='', max_length=255)
    reason_2_icon = models.CharField(verbose_name='Иконка причины 2', default='', max_length=255)

    reason_3_title = models.CharField(verbose_name='Название причины 3', default='', max_length=255)
    reason_3_text = models.CharField(verbose_name='Текст причины 3', default='', max_length=255)
    reason_3_icon = models.CharField(verbose_name='Иконка причины 3', default='', max_length=255)

    reason_4_title = models.CharField(verbose_name='Название причины 4', default='', max_length=255)
    reason_4_text = models.CharField(verbose_name='Текст причины 4', default='', max_length=255)
    reason_4_icon = models.CharField(verbose_name='Иконка причины 4', default='', max_length=255)

    reason_5_title = models.CharField(verbose_name='Название причины 5', default='', max_length=255)
    reason_5_text = models.CharField(verbose_name='Текст причины 5', default='', max_length=255)
    reason_5_icon = models.CharField(verbose_name='Иконка причины 5', default='', max_length=255)

    reason_6_title = models.CharField(verbose_name='Название причины 6', default='', max_length=255)
    reason_6_text = models.CharField(verbose_name='Текст причины 6', default='', max_length=255)
    reason_6_icon = models.CharField(verbose_name='Иконка причины 6', default='', max_length=255)

    under_text = models.TextField(verbose_name='Текст внизу секции', default='', max_length=255)

    def __str__(self):
        return 'Секция WhyUs'

    class Meta:
        verbose_name = 'Секция WhyUs'
        verbose_name_plural = 'Секция WhyUs'


class SkillsSection(models.Model):
    """Модель для секции Skills"""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)

    skill_1_title = models.CharField(verbose_name='Название принципа 1', default='', max_length=255)
    skill_1_value = models.IntegerField(verbose_name='Значение принципа 1', default=0)

    skill_2_title = models.CharField(verbose_name='Название принципа 2', default='', max_length=255)
    skill_2_value = models.IntegerField(verbose_name='Значение принципа 2', default=0)

    skill_3_title = models.CharField(verbose_name='Название принципа 3', default='', max_length=255)
    skill_3_value = models.IntegerField(verbose_name='Значение принципа 3', default=0)

    def __str__(self):
        return 'Секция Skills'

    class Meta:
        verbose_name = 'Секция Skills'
        verbose_name_plural = 'Секция Skills'


class ServicesSection(models.Model):
    """Модель для секции Services"""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)

    service_1_title = models.CharField(verbose_name='Название услуги 1', default='', max_length=255)
    service_1_text = models.CharField(verbose_name='Описание услуги 1', default='', max_length=255)
    service_1_icon = models.CharField(verbose_name='Иконка услуги 1', default='', max_length=255)

    service_2_title = models.CharField(verbose_name='Название услуги 2', default='', max_length=255)
    service_2_text = models.CharField(verbose_name='Описание услуги 2', default='', max_length=255)
    service_2_icon = models.CharField(verbose_name='Иконка услуги 2', default='', max_length=255)

    service_3_title = models.CharField(verbose_name='Название услуги 3', default='', max_length=255)
    service_3_text = models.CharField(verbose_name='Описание услуги 3', default='', max_length=255)
    service_3_icon = models.CharField(verbose_name='Иконка услуги 3', default='', max_length=255)

    def __str__(self):
        return 'Секция Services'

    class Meta:
        verbose_name = 'Секция Services'
        verbose_name_plural = 'Секция Services'


class QuoteSection(models.Model):
    """Модель для секции Quote"""
    text = models.TextField(verbose_name='Текст', default='')

    def __str__(self):
        return 'Секция Quote'

    class Meta:
        verbose_name = 'Секция Quote'
        verbose_name_plural = 'Секция Quote'
