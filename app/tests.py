from django.test import TestCase

# Create your tests here.
from   django.test import  TestCase
from   django.urls import  resolve
from   app.views import home_page
from   django.http import HttpResponse
from   django.template.loader import render_to_string
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)

class HomePageTest(TestCase):
    # def test_root_url_resolve_to_home_page_view(self):
    #     found = resolve('/app/home')
    #     self.assertEqual(found.func,home_page)

    # def test_home_page_returns_correct_html(self):
        # request = HttpResponse()
        # response = home_page(request)
        # html=response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # expectd_html = render_to_string('home.html')
        # self.assertEqual(html,expectd_html)

        # response = self.client.get('/app/home')
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))
        # self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/app/home')
        self.assertTemplateUsed(response, 'home.html')

