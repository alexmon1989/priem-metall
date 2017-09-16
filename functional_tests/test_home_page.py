from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os, time


class TestBase(StaticLiveServerTestCase):
    fixtures = ['home_section.json', 'about_section.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()


class HomeSectionTest(TestBase):

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


class AboutSectionTest(TestBase):

    def test_correct_info(self):
        # Пользователь заходит на сайт
        self.browser.get(self.live_server_url)

        # Смотрит на секцию Home и видит там верную инофрмацию
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                'section#about.bg-white div.container div.row.justify-content-center.pb-5 div.col-lg-9.pb-lg-4'
                '.text-center h3.font-alt.font-w-600.letter-spacing-2.text-uppercase.title-xs-small.title-extra-large-2'
            ).text,
            "Кто мы?".upper()
        )
        self.assertEqual(
            self.browser.find_element_by_css_selector(
                'section#about.bg-white div.container div.row.justify-content-center.pb-5 '
                'div.col-lg-9.pb-lg-4.text-center p.font-alt.mb-0.mt-3.text-xs-large.text-uppercase.title-medium'
            ).text,
            "Несколько вещей, которые вам стоит знать о нас".upper()
        )
        self.assertInHTML(
            "Gunung Rinjani adalah nama sebuah gunung yang berlokasi di Pulau Lombok, Nusa Tenggara Barat. Gunung ini merupakan gunung favorit bagi pendaki Indonesia karena keindahan pemandangannya.",
            self.browser.find_element_by_css_selector(
                'html body#page-top.pace-running section#about.bg-white '
                'div.container div.row div.col-lg-6 div.pl-lg-4.pt-5.pt-lg-0'
            ).get_attribute('innerHTML')
        )
        self.assertInHTML(
            "Gunung ini merupakan bagian dari Taman Nasional Gunung Rinjani yang memiliki luas sekitar 41.330 ha dan ini akan segera diusulkan penambahannya sehingga menjadi 76.000 ha. Secara administratif gunung ini berada dalam wilayah tiga kabupaten: Lombok Timur, Lombok Tengah dan Lombok Barat. ",
            self.browser.find_element_by_css_selector(
                'html body#page-top.pace-running section#about.bg-white '
                'div.container div.row div.col-lg-6 div.pl-lg-4.pt-5.pt-lg-0'
            ).get_attribute('innerHTML')
        )
        self.assertInHTML(
            "Gunung ini merupakan bagian dari Taman Nasional Gunung Rinjani yang memiliki.",
            self.browser.find_element_by_css_selector(
                'html body#page-top.pace-running section#about.bg-white '
                'div.container div.row div.col-lg-6 div.pl-lg-4.pt-5.pt-lg-0'
            ).get_attribute('innerHTML')
        )
        self.assertInHTML(
            "<img src=\"media/uploads/about-1.jpg\" alt=\"\" class=\"img-fluid box-shadow-shallow rounded\">",
            self.browser.find_element_by_css_selector(
                'section#about.bg-white div.container div.row div.col-lg-6 div.carousel-custom.flickity-enabled '
                'div.flickity-viewport div.flickity-slider'
            ).get_attribute('innerHTML')
        )
        self.assertInHTML(
            "<img src=\"media/uploads/about-2.jpg\" alt=\"\" class=\"img-fluid box-shadow-shallow rounded\">",
            self.browser.find_element_by_css_selector(
                'section#about.bg-white div.container div.row div.col-lg-6 div.carousel-custom.flickity-enabled '
                'div.flickity-viewport div.flickity-slider'
            ).get_attribute('innerHTML')
        )
        self.assertInHTML(
            "<img src=\"media/uploads/about-3.jpg\" alt=\"\" class=\"img-fluid box-shadow-shallow rounded\">",
            self.browser.find_element_by_css_selector(
                'section#about.bg-white div.container div.row div.col-lg-6 div.carousel-custom.flickity-enabled '
                'div.flickity-viewport div.flickity-slider'
            ).get_attribute('innerHTML')
        )
