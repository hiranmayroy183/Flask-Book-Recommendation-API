import unittest
from flask_testing import TestCase
from app import app

class TestBookRecommendationAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_recommendations_no_author(self):
        response = self.client.get('/recommend?page=1&per_page=5')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('total', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('data', data)
        self.assertIsInstance(data['data'], list)

    def test_recommendations_with_author(self):
        response = self.client.get('/recommend?author=Rowling&page=1&per_page=5')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('total', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)
        self.assertIn('data', data)
        self.assertIsInstance(data['data'], list)
        for item in data['data']:
            self.assertIn('authors', item)
            self.assertIn('Rowling', item['authors'])

    def test_invalid_page(self):
        response = self.client.get('/recommend?page=invalid')
        self.assertEqual(response.status_code, 400)  # Expecting 400 for invalid page
        self.assertIn('error', response.json)

    def test_invalid_per_page(self):
        response = self.client.get('/recommend?per_page=invalid')
        self.assertEqual(response.status_code, 400)  # Expecting 400 for invalid per_page
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
