from django.test import TestCase
from home.models import HomeSection


class ListAndItemModelsTest(TestCase):

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
