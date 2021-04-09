from django.test import TestCase

# Create your tests here.
from   django.test import  TestCase
from   django.urls import  resolve
from   app.views import home_page
from   django.http import HttpResponse
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/app/home')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = home_page(request)
        html=response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))