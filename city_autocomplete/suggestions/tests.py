from django.test import TestCase, Client
from .models import City

class SuggestionsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name='New York',  latitude=40.7128, longitude=74.0060)


    def test_suggestions(self):
        response = self.client.get('/suggestions/', {'q': 'New'})
        self.assertEqual(response.status_code, 200)
        suggestions = response.json()['suggestions']
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]['name'], 'New York')