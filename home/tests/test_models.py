from django.test import TestCase
from home.models import HomeSection, AboutSection


class HomeSectionModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        home_section = HomeSection()
        home_section.text_1 = 'Добро пожаловать'
        home_section.text_2 = 'Приём и вывоз металлолома в Киеве'
        home_section.text_3 = 'Дорого купим ваш металлолом. Свяжитесь с нами и убедитесь, что наши цены - лучшие на рынке.'
        home_section.text_4 = 'Узнать больше'
        home_section.text_5 = 'Gunung Rinjani merupakan salah satu destinasi gunung favorit bagi para pendaki di Indonesia dikarenakan keindahan pemandangan alamnya. Gunung Rinjani berlokasi di Pulau Lombok, Nusa Tenggara Barat.'
        home_section.save()

        home_section_saved = HomeSection.objects.first()
        self.assertEqual(home_section_saved.text_1, 'Добро пожаловать')
        self.assertEqual(home_section_saved.text_2, 'Приём и вывоз металлолома в Киеве')
        self.assertEqual(
            home_section_saved.text_3,
            'Дорого купим ваш металлолом. Свяжитесь с нами и убедитесь, что наши цены - лучшие на рынке.'
        )
        self.assertEqual(home_section_saved.text_4, 'Узнать больше')
        self.assertEqual(
            home_section_saved.text_5,
            'Gunung Rinjani merupakan salah satu destinasi gunung favorit bagi para pendaki di Indonesia dikarenakan keindahan pemandangan alamnya. Gunung Rinjani berlokasi di Pulau Lombok, Nusa Tenggara Barat.'
        )


class AboutSectionModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        about_section = AboutSection()
        about_section.title = 'О нас'
        about_section.under_title = 'Несколько вещей, которые вам стоит знать о нас'
        about_section.text = 'Gunung Rinjani adalah nama sebuah gunung yang berlokasi di Pulau Lombok, ' \
                             'Nusa Tenggara Barat. Gunung ini merupakan gunung favorit bagi pendaki ' \
                             'Indonesia karena keindahan pemandangannya.'
        about_section.image_1 = 'static/assets/images/about-1.jpg'
        about_section.image_2 = 'static/assets/images/about-3.jpg'
        about_section.image_3 = 'static/assets/images/about-3.jpg'

        about_section.save()

        about_section_saved = AboutSection.objects.first()
        self.assertEqual(about_section_saved.title, 'О нас')
        self.assertEqual(about_section_saved.under_title, 'Несколько вещей, которые вам стоит знать о нас')
        self.assertEqual(
            about_section_saved.text,
            'Gunung Rinjani adalah nama sebuah gunung yang berlokasi di Pulau Lombok,'
            ' Nusa Tenggara Barat. Gunung ini merupakan gunung favorit bagi pendaki '
            'Indonesia karena keindahan pemandangannya.'
        )
        self.assertEqual(about_section_saved.image_1, 'static/assets/images/about-1.jpg')
        self.assertEqual(about_section_saved.image_2, 'static/assets/images/about-3.jpg')
        self.assertEqual(about_section_saved.image_3, 'static/assets/images/about-3.jpg')
