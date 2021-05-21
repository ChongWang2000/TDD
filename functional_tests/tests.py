# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import unittest
from selenium import webdriver
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()  # 1

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. she goes to check out its homepage
        # self.browser.get('http://localhost:8000/app/home')
        self.browser.get(self.live_server_url + "/app/home")

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "Buy peacock feathers" into a text box(Edith`s hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # "1:Buy peacock 'feathers' as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # there is still a text box inviting her to add another item. she enters "use peacock feathers to make a fly"(Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. then she sees
        # that the site has generated a unique URL for her -- there is some explanatory text to that effect
        self.fail('Finish the test')
        # she visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep


    def test_can_start_a_list_for_one_user(self):

        #Edith has heard about a cool new online to-do app. she goes
        #the page updates again, and now show both items on her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #satisfied, she goes back to sleep


    def test_mutiple_users_can_start_lists_at_different_urls(self):
        #Edith starts a new to-do list
        self.browser.get(self.live_server_url+"/app/home")
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #she notices that her list has a unique URL
        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/list/.+')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url+"/app/home")
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,'lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)