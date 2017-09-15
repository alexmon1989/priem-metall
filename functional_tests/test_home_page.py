from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os


class TestBase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()


class HomeSectionTest(TestBase):
    fixtures = ['home_section.json']

    def test_correct_info(self):
        # Пользователь заходит на сайт
        self.browser.get(self.live_server_url)

        # Смотрит на секцию Home и видит там верную инофрмацию
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                '#home-bg-parallax span.d-block.font-alt.font-w-600.letter-spacing-2'
                '.text-medium.text-uppercase.text-white'
            ).text,
            "Добро пожаловать".upper()
        )
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                '#home-bg-parallax h1.font-alt.font-w-600.letter-spacing-2.mb-3.mt-3'
                '.text-uppercase.text-white.title-xs-extra-large.title-extra-large-3'
            ).text,
            "Приём и вывоз металлолома в Киеве".upper()
        )
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                '#home-bg-parallax span.d-block.font-alt.letter-spacing-2.mb-3.mt-4'
                '.text-large.text-uppercase.text-white'
            ).text,
            "Дорого купим ваш металлолом. Свяжитесь с нами и убедитесь, что наши цены - лучшие на рынке.".upper()
        )
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                '#home-bg-parallax a.page-scroll.btn.btn-base-color.btn-large.btn-shadow.mr-0.mt-4'
            ).text,
            "Узнать больше".upper()
        )
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                '.intro p.font-alt.mb-0.text-xs-large.text-extra-large'
            ).text,
            "Gunung Rinjani merupakan salah satu destinasi gunung favorit bagi para pendaki di "
            "Indonesia dikarenakan keindahan pemandangan alamnya. Gunung Rinjani berlokasi di Pulau "
            "Lombok, Nusa Tenggara Barat."
        )
