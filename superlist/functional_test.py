# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import django
from selenium import webdriver
import unittest


from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit() # 1

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. she goes to check out its homepage
        self.browser.get('http://localhost:8000/app/home')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
#
# # she is invited to enter a to-do item straight away
#
# # she types "Buy peacock feathers" into a text box(Edith`s hobby is tying fly-fishing lures)
#
# # when she hits enter, the page updates, and now the page lists
# # "1:Buy peacock 'feathers' as an item in a to-do list
#
# # there is still a text box inviting her to add another item. she enters "use peacock feathers to make a fly"(Edith is very methodical)
#
# # the page updates again, and now shows both items on her list
#
# # Edith wonders whether the site will remember her list. then she sees
# # that the site has generated a unique URL for her -- there is some explanatory text to that effect
#
# # she visits that URL - her to-do list is still there
#
# # Satisfied, she goes back to sleep

