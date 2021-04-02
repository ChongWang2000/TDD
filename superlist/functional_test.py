# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import django
from selenium import webdriver
import unittest


def test():
    browser = webdriver.Firefox()

    # Edith has heard about a cool new online to-do app.
    # She goes to check out its homepage
    browser.get("http://localhost:8000/")

    # She notices the page title and header mention to-do lists
    assert 'To-Do' in browser.title
    print(browser.title)


# She is invited tp enter to-do item straight away

# She types "Buy peacock features" into a twxt box
# Edith's hobby is trying fly-fishing lures

# When she hits enter, the pages updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both item on her list

# Edith wonder whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep

# browser.quit()


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
