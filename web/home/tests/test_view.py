from django.test import TestCase
from django.urls import resolve

from home.views import HomePage


class TestHomePageView(TestCase):

    def test_root_url_resolves_to_home_page(self):
        response = resolve('/')
        self.assertEqual(response.func.__name__, HomePage.as_view().__name__)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertIn('<html', html)
        self.assertIn('<body', html)
        self.assertIn('<title>Facebook Login App</title>', html)
        self.assertTrue(html.endswith('</html>'))
