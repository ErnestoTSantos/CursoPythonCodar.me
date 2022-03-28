import json

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Category


class TestListingCategories(APITestCase):
    def test_listing_empty(self):
        response = self.client.get('/api/categories/?format=json')
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_listing_categories(self):
        Category.objects.create(name='MotoGP', pilots_amount=28, motorization=1000, last_champion='Fabio Quartararo')  # noqa:E501
        Category.objects.create(name='Moto2', pilots_amount=34, motorization=765, last_champion='Remy Gardner')  # noqa:E501

        response = self.client.get('/api/categories/?format=json')
        data = json.loads(response.content)
        elements = [
            {
                'id': 1,
                'name': 'MotoGP',
                'pilots_amount': 28,
                'motorization': 1000,
                'last_champion': 'Fabio Quartararo'
            },
            {
                'id': 2,
                'name': 'Moto2',
                'pilots_amount': 34,
                'motorization': 765,
                'last_champion': 'Remy Gardner'
            },
        ]

        self.assertEqual(data, elements)


class TestCreateCategory(APITestCase):
    def test_create_category(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        category_request_data = {
            'name': 'Moto2',
            'pilots_amount': 34,
            'motorization': 765,
            'last_champion': 'Remy Gardner'
        }

        self.client.force_authenticate(user)
        response = self.client.post('/api/categories/', category_request_data)
        response_get = self.client.get('/api/categories/?format=json')

        category_comparasion_data = {
            'id': 1,
            'name': 'Moto2',
            'pilots_amount': 34,
            'motorization': 765,
            'last_champion': 'Remy Gardner'
        }

        data = json.loads(response_get.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data[0], category_comparasion_data)

    def test_return_400_when_invalid(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        category_request_data = {
            'name': 983,
            'pilots_amount': 34,
            'motorization': 765,
            'last_champion': 'Remy Gardner'
        }

        self.client.force_authenticate(user)
        response = self.client.post('/api/categories/', category_request_data)

        self.assertEqual(response.status_code, 400)


class TestDetailCategory(APITestCase):
    def test_get_detail_category(self):
        Category.objects.create(name='Moto2', pilots_amount=34, motorization=765, last_champion='Remy Gardner')  # noqa:E501
        response = self.client.get('/api/categories/details/Moto2/?format=json')  # noqa:E501
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Moto2')
        self.assertEqual(data['pilots_amount'], 34)
        self.assertEqual(data['motorization'], 765)
        self.assertEqual(data['last_champion'], 'Remy Gardner')

    def test_patch_category(self):
        Category.objects.create(name='Moto2', pilots_amount=34, motorization=765, last_champion='Remy Gardner')  # noqa:E501
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        self.client.force_authenticate(user)

        url = '/api/categories/details/Moto2/?format=json'
        response = self.client.patch(url, {'name': 'MotoGP'})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'MotoGP')

    def test_delete_category(self):
        Category.objects.create(name='Moto2', pilots_amount=34, motorization=765, last_champion='Remy Gardner')  # noqa:E501
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501

        url = '/api/categories/details/Moto2/?format=json'
        self.client.force_authenticate(user)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
