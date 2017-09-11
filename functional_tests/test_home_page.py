from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_can_view_home_page(self):
        # Пользователь заходит на сайт
        self.browser.get(self.live_server_url)

        # смотрит тот ли это сайт
        self.assertIn('металлолом', self.browser.title)
