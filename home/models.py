from django.db import models
from django.db.models.signals import post_save
from django.core.cache import cache
from django.dispatch import receiver


@receiver(post_save)
def clear_the_cache(**kwargs):
    cache.clear()


class HomeSection(models.Model):
    """Модель для секции Home."""
    text_1 = models.CharField(verbose_name='Текст 1', default='', max_length=255)
    text_2 = models.CharField(verbose_name='Текст 2 (тег h1)', default='', max_length=255)
    text_3 = models.CharField(verbose_name='Текст 3', default='', max_length=255)
    text_4 = models.TextField(verbose_name='Текст 4', default='')
    text_5 = models.CharField(verbose_name='Текст 5', default='', max_length=255)
    text_6 = models.CharField(verbose_name='Текст 6', default='', max_length=255)

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

    service_4_title = models.CharField(verbose_name='Название услуги 4', default='', max_length=255)
    service_4_text = models.CharField(verbose_name='Описание услуги 4', default='', max_length=255)
    service_4_icon = models.CharField(verbose_name='Иконка услуги 4', default='', max_length=255)

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


class PricingSection(models.Model):
    """Модель для секции Pricing"""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)
    text = models.TextField(verbose_name='Текст', default='')

    def __str__(self):
        return 'Секция Pricing'

    class Meta:
        verbose_name = 'Секция Pricing'
        verbose_name_plural = 'Секция Pricing'


class JobSchemeSection(models.Model):
    """Модель для секции JobScheme"""
    title = models.CharField(verbose_name='Заглавие', default='', max_length=255)
    under_title = models.CharField(verbose_name='Текст под заглавием', default='', max_length=255)

    item_1_title = models.CharField(verbose_name='Название пункта 1', default='', max_length=255)
    item_1_text = models.TextField(verbose_name='Текст пункта 1', default='')
    item_1_image = models.ImageField(verbose_name='Изображение пункта 1', upload_to='uploads/')

    item_2_title = models.CharField(verbose_name='Название пункта 2', default='', max_length=255)
    item_2_text = models.TextField(verbose_name='Текст пункта 2', default='')
    item_2_image = models.ImageField(verbose_name='Изображение пункта 1', upload_to='uploads/')

    item_3_title = models.CharField(verbose_name='Название пункта 3', default='', max_length=255)
    item_3_text = models.TextField(verbose_name='Текст пункта 3', default='')
    item_3_image = models.ImageField(verbose_name='Изображение пункта 3', upload_to='uploads/')

    item_4_title = models.CharField(verbose_name='Название пункта 3', default='', max_length=255)
    item_4_text = models.TextField(verbose_name='Текст пункта 3', default='')
    item_4_image = models.ImageField(verbose_name='Изображение пункта 3', upload_to='uploads/')

    item_5_title = models.CharField(verbose_name='Название пункта 3', default='', max_length=255)
    item_5_text = models.TextField(verbose_name='Текст пункта 3', default='')
    item_5_image = models.ImageField(verbose_name='Изображение пункта 3', upload_to='uploads/')

    under_text = models.TextField(verbose_name='Текст внизу секции', default='', max_length=255)

    def __str__(self):
        return 'Секция JobScheme'

    class Meta:
        verbose_name = 'Секция JobScheme'
        verbose_name_plural = 'Секция JobScheme'


class TestimonialsSection(models.Model):
    """Модель для секции Testimonials"""
    item_1_name = models.CharField(verbose_name='Имя клиента 1', default='', max_length=255)
    item_1_position = models.CharField(verbose_name='Должность клиента 1', default='', max_length=255)
    item_1_image = models.ImageField(verbose_name='Изображение клиента 1', upload_to='uploads/')
    item_1_text = models.TextField(verbose_name='Текст отзыва 1', default='')

    item_2_name = models.CharField(verbose_name='Имя клиента 2', default='', max_length=255)
    item_2_position = models.CharField(verbose_name='Должность клиента 2', default='', max_length=255)
    item_2_image = models.ImageField(verbose_name='Изображение клиента 2', upload_to='uploads/')
    item_2_text = models.TextField(verbose_name='Текст отзыва 2', default='')

    item_3_name = models.CharField(verbose_name='Имя клиента 3', default='', max_length=255)
    item_3_position = models.CharField(verbose_name='Должность клиента 3', default='', max_length=255)
    item_3_image = models.ImageField(verbose_name='Изображение клиента 3', upload_to='uploads/')
    item_3_text = models.TextField(verbose_name='Текст отзыва 3', default='')

    def __str__(self):
        return 'Секция Testimonials'

    class Meta:
        verbose_name = 'Секция Testimonials'
        verbose_name_plural = 'Секция Testimonials'


class ContactsSection(models.Model):
    """Модель для секции Contacts"""
    phones_text = models.TextField(verbose_name='Текст блока телефонов', default='')
    address_text = models.TextField(verbose_name='Текст блока адреса', default='')

    def __str__(self):
        return 'Секция Contacts'

    class Meta:
        verbose_name = 'Секция Contacts'
        verbose_name_plural = 'Секция Contacts'


class HeaderContactsSection(models.Model):
    """Модель для секции Contacts"""
    phone_1 = models.CharField(verbose_name='Телефон 1', default='', max_length=255)
    phone_2 = models.CharField(verbose_name='Телефон 2', default='', max_length=255)
    address = models.CharField(verbose_name='Адрес', default='', max_length=255)

    def __str__(self):
        return 'Секция HeaderContacts'

    class Meta:
        verbose_name = 'Секция HeaderContacts'
        verbose_name_plural = 'Секция HeaderContacts'


class SeoSettings(models.Model):
    """Модель для секции Contacts"""
    title = models.CharField(verbose_name='Title', default='', max_length=255)
    description = models.CharField(verbose_name='Description', default='', max_length=255)
    keywords = models.CharField(verbose_name='keywords', default='', max_length=255)

    def __str__(self):
        return 'Настройки SEO (метатеги)'

    class Meta:
        verbose_name = 'Настройки SEO (метатеги)'
        verbose_name_plural = 'Настройки SEO (метатеги)'
