from django.test import TestCase
from home.models import HomeSection, AboutSection


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')


class HomeSectionTest(TestCase):

    def test_section_returns_correct_html(self):
        home_section = HomeSection()
        home_section.text_1 = 'Текст 1'
        home_section.text_2 = 'Текст 2'
        home_section.text_3 = 'Текст 3'
        home_section.text_4 = 'Текст 4'
        home_section.text_5 = 'Текст 5'
        home_section.save()

        response = self.client.get('/')

        self.assertContains(response, 'Текст 1')
        self.assertContains(response, 'Текст 2')
        self.assertContains(response, 'Текст 3')
        self.assertContains(response, 'Текст 4')
        self.assertContains(response, 'Текст 5')


class AboutSectionTest(TestCase):

    def test_section_returns_correct_html(self):
        home_section = AboutSection()
        home_section.title = 'home_section.title'
        home_section.under_title = 'home_section.under_title'
        home_section.text = 'home_section.text'
        home_section.image_1 = 'home_section.image_1'
        home_section.image_2 = 'home_section.image_2'
        home_section.image_3 = 'home_section.image_3'
        home_section.save()

        response = self.client.get('/')

        self.assertContains(response, 'home_section.title')
        self.assertContains(response, 'home_section.under_title')
        self.assertContains(response, 'home_section.text')
        self.assertContains(response, 'home_section.image_1')
        self.assertContains(response, 'home_section.image_2')
        self.assertContains(response, 'home_section.image_3')
