# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author: Justin Welenofsky, Most code copied shamelessly from      #
#   TDD Development                                                 #
# Description: Functional Tests, also called                        #
#   black box, end-to-end or acceptance Tests                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

DEFAULT_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_host = arg.split('=')[1]
                cls.server_url = 'http://' + cls.server_host
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if not cls.against_staging:
            super().tearDownClass()

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('startup.homepage_welcome_url.additional', '')
        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')