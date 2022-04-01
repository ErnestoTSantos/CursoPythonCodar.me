import json
from datetime import datetime, timezone
from unittest import mock

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from schedule.models import Employee, Establishment, Faithfulness, Scheduling


class TestingReturnedName(APITestCase):
    def test_returned_name_in_scheduling(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        scheduling = Scheduling.objects.create(provider=user, date_time='2022-04-28T15:00Z', client_name='Matheus Silva', client_phone='(51) 93920-0394')  # noqa:E501

        assert str(scheduling) == 'Matheus Silva'

    def test_returned_name_in_faithfulness(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        faithfulness = Faithfulness.objects.create(
            provider=user, client='Matheus Silva')

        assert str(faithfulness) == 'Matheus Silva = 0'

    def test_returned_name_in_establishment(self):
        establishment = Establishment.objects.create(name='Python Barber shop')

        assert str(establishment) == 'Python Barber shop'

    def test_returned_name_in_employee(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        establishment = Establishment.objects.create(name='Python Barber shop')
        employee = Employee.objects.create(provider=user, establishment=establishment, assignment='Cortar cabelo')  # noqa:E501

        assert str(employee) == 'Ernesto -> Python Barber shop'


class TestListingScheduling(APITestCase):
    def test_listing_empty(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        self.client.force_authenticate(user)
        response = self.client.get('/api/scheduling/?username=Ernesto')
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_listing_schedulings(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Scheduling.objects.create(provider=user, date_time='2022-04-28T17:30:00Z', client_name='Ernesto Santos', client_email='ernesto.terra2003@gmail.com', client_phone='(51) 98936-5022')  # noqa:E501
        self.client.force_authenticate(user)
        response = self.client.get('/api/scheduling/?username=Ernesto')
        data = json.loads(response.content)
        scheduling_serialized = {
            'id': 1,
            'provider': 'Ernesto',
            'date_time': '2022-04-28T17:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022',
            'confirmed': False,
            'states': 'NCNF'
        }
        self.assertEqual(data[0], scheduling_serialized)


class TestCreateScheduling(APITestCase):
    def test_create_scheduling(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T14:30:00-00:00',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        self.client.force_authenticate(user)
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        scheduling_create = Scheduling.objects.get()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(scheduling_create.provider, user)
        self.assertEqual(scheduling_create.date_time, datetime(2022, 4, 28, 14, 30, tzinfo=timezone.utc))  # noqa:E501
        self.assertEqual(scheduling_create.client_name, 'Ernesto Santos')  # noqa:E501
        self.assertEqual(scheduling_create.client_email, 'ernesto.terra2003@gmail.com')  # noqa:E501
        self.assertEqual(scheduling_create.client_phone, '(51) 98936-5022')  # noqa:E501

    def test_create_scheduling_in_past(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2020-04-28T14:30:00-00:00',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501

        self.assertEqual(response.status_code, 400)

    def test_create_scheduling_with_get(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        url = '/api/scheduling/?establishment=Ruby barber shop'
        self.client.force_authenticate(user)
        response = self.client.post(url, scheduling_request_data)  # noqa:E501
        response_get = self.client.get('/api/scheduling/?username=Ernesto')
        data = json.loads(response_get.content)
        scheduling_element = data[0]

        self.assertEqual(response.status_code, 201)
        self.assertEqual(scheduling_element['date_time'], scheduling_request_data['date_time'])  # noqa:E501
        self.assertEqual(scheduling_element['client_name'], scheduling_request_data['client_name'])  # noqa:E501
        self.assertEqual(scheduling_element['client_email'], scheduling_request_data['client_email'])  # noqa:E501
        self.assertEqual(scheduling_element['client_phone'], scheduling_request_data['client_phone'])  # noqa:E501

    def test_return_400_when_invalid(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T17:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003',
            'client_phone': '(51) 98936-5022'
        }
        self.client.force_authenticate(user)
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501

        self.assertEqual(response.status_code, 400)


class TestDetailScheduling(APITestCase):
    def test_get_object(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        self.client.force_authenticate(user)
        url = '/api/scheduling/1/?username=Ernesto'
        response_get = self.client.get(url)
        data = json.loads(response_get.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['date_time'], scheduling_request_data['date_time'])  # noqa:E501
        self.assertEqual(data['client_name'], scheduling_request_data['client_name'])  # noqa:E501
        self.assertEqual(data['client_email'], scheduling_request_data['client_email'])  # noqa:E501
        self.assertEqual(data['client_phone'], scheduling_request_data['client_phone'])  # noqa:E501

    def test_patch_object(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501]
        url = '/api/scheduling/1/'
        self.client.force_authenticate(user)
        response_patch = self.client.patch(url, {'client_name': 'Ernesto Terra dos Santos'})  # noqa:E501
        response_get = self.client.get(url + '?username=Ernesto')
        data = json.loads(response_get.content)

        self.assertEqual(response_patch.status_code, 200)
        self.assertEqual(data['client_name'], 'Ernesto Terra dos Santos')

    def test_delete_object(self):
        user = User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        self.client.force_authenticate(user)
        url = '/api/scheduling/1/'
        response_delete = self.client.delete(url)

        self.assertEqual(response_delete.status_code, 204)


class TestGetHorary(APITestCase):
    @mock.patch('schedule.utils.is_holiday', return_value=True)
    def test_when_date_is_holiday_return_empty(self, is_holiday_mock):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        response = self.client.get('/api/horary/2022-12-25/?username=Ernesto')
        data = json.loads(response.content)

        self.assertEqual(data, [])  # noqa:E501

    @mock.patch('schedule.utils.is_holiday', return_value=False)
    def test_when_date_is_common(self, is_holiday_mock):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        response = self.client.get('/api/horary/2022-04-28/?username=Ernesto')
        data = json.loads(response.content)

        self.assertNotEqual(data, [])
        self.assertEqual(data[0], {'date_time': '2022-04-28T09:00:00'})
        self.assertEqual(data[-1], {'date_time': '2022-04-28T17:30:00'})


class TestSerializerScheduling(APITestCase):
    def test_validate_provider_return_error(self):
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-28T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'provider': ['Username não existe!']}

    def test_validate_date_time_when_day_is_sunday(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-03T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'date_time': ['Infelizmente o estabelecimento não trabalha aos domingos!']}  # noqa:E501

    def test_validate_date_time_when_day_is_saturday(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-02T14:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'date_time': ['Infelizmente o estabelecimento só trabalha até as 13h no sábado!']}  # noqa:E501

    def test_validate_date_time_when_is_lunch_time(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T12:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'date_time': ['Os funcionários estão no horário de almoço!']}  # noqa:E501

    def test_validate_date_time_when_time_is_earlier_than_opening_time(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T8:30:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'date_time': ['O estabelecimento abre apenas às 9h!']}  # noqa:E501

    def test_validate_date_time_when_time_is_more_latest_than_closing_time(self):  # noqa:E501
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T18:00:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'date_time': ['O estabelecimento fehca às 18h!']}  # noqa:E501

    def test_validate_client_name_characters(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T17:00:00Z',
            'client_name': 'Ana',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'client_name': ['O nome do cliente precisa ter 7 ou mais caracteres!']}  # noqa:E501

    def test_validate_client_name_space_for_last_name(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T17:00:00Z',
            'client_name': 'Ernesto',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'client_name': ['O cliente precisa ter um sobrenome!']}  # noqa:E501

    def test_validate_client_phone_characters(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T17:00:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'client_phone': ['O número de telefone precisa ter no mínimo 8 digitos!']}  # noqa:E501

    def test_validate_client_phone_valid_characters(self):
        User.objects.create(email='ernesto.terra2003@gmail.com', username='Ernesto', password='12345')  # noqa:E501
        Establishment.objects.create(name='Ruby barber shop')
        scheduling_request_data = {
            'provider': 'Ernesto',
            'date_time': '2022-04-01T17:00:00Z',
            'client_name': 'Ernesto Santos',
            'client_email': 'ernesto.terra2003@gmail.com',
            'client_phone': '(51) 98936-5022*'
        }
        response = self.client.post('/api/scheduling/?establishment=Ruby barber shop', scheduling_request_data)  # noqa:E501
        data = json.loads(response.content)

        assert response.status_code == 400
        assert data == {'client_phone': ['O número pode ter apenas valores entre 0-9, parenteses, traços, espaço e o sinal de mais!']}  # noqa:E501
