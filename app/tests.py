from django.test import TestCase

# Create your tests here.
from   django.test import  TestCase
from   django.urls import  resolve
from   app.views import home_page
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/app/home')
        self.assertEqual(found.func,home_page)