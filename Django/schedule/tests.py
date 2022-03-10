from datetime import date

from django.forms import ValidationError
from django.test import Client, TestCase
from django.urls import resolve, reverse

from schedule.models import Category, Event
from schedule.views import (category_datails, display_event, list_category,
                            list_events)


class TestInitialPage(TestCase):
    def test_list_events(self):
        # Estamos testando para onde a página inicial está enviando o usuário
        client = Client()
        response = client.get('/')

        # self.assertContains(response, '<th>Nome</th>')
        self.assertTemplateUsed(response, 'schedule/events/listing_events.html')  # noqa:E501

    def test_source_path_url_is_correct(self):
        url = reverse('schedule:source')
        self.assertEqual(url, '/')


class TestListingEvents(TestCase):
    def test_events_with_today_date(self):
        category = Category.create_class('Back-end')
        event = Event.create_event('Python class', category, date.today(), place='Rio de Janeiro')  # noqa:E501
        javascript = Event.create_event('javascript class', category, date.today(), place='Florianópolis')  # noqa:E501
        ruby = Event.create_event('Ruby class', category, date.today(), place='Garopaba')  # noqa:E501
        php = Event.create_event('PHP class', category, date.today(), place='Canoas')  # noqa:E501

        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Python class')
        # Aqui nós estamos acessando o que vem no contexto da página
        self.assertEqual(response.context['events'][0], event)
        self.assertEqual(response.context['events'][1], javascript)
        self.assertEqual(response.context['events'][2], ruby)
        # Aqui convertemos o queryset para uma lista e comparamos os elementos
        self.assertEqual(list(response.context['events']), [event, javascript, ruby, php])  # noqa:E501

    def test_events_without_date(self):
        category = Category.create_class('Back-end')
        event = Event.create_event('Python class', category, date=None, place='Rio de Janeiro')  # noqa:E501
        javascript = Event.create_event('javascript class', category, date=None, place='Florianópolis')  # noqa:E501

        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Python class')
        self.assertContains(response, 'A definir')
        self.assertEqual(response.context['events'][0], event)
        self.assertEqual(response.context['events'][1], javascript)
        self.assertEqual(list(response.context['events']), [event, javascript])  # noqa:E501

    def test_no_registered_events(self):
        client = Client()
        response = client.get('/')

        self.assertContains(response, 'Infelizmente não temos eventos cadastrados para os próximos dias!')  # noqa:E501

    def test_listing_events_uses_correct_view_function(self):
        view = resolve(reverse('schedule:index'))
        self.assertEqual(view.func, list_events)

    def test_listing_events_url_is_correct(self):
        url = reverse('schedule:index')
        self.assertEqual(url, '/events/')


class TestDisplayEvent(TestCase):
    def test_not_found_return_404(self):
        client = Client()
        response = client.get(reverse('schedule:details', kwargs={'id': 100}))
        self.assertEqual(response.status_code, 404)

    def test_used_template_on_display(self):
        client = Client()
        category = Category.create_class('Back-end')
        javascript = Event.create_event('javascript class', category, date=None, place='Florianópolis')  # noqa:E501
        response = client.get(reverse('schedule:details', kwargs={'id': 1}))

        self.assertTemplateUsed(response, 'schedule/events/display_event.html')  # noqa:E501

    def test_display_event(self):
        client = Client()
        category = Category.create_class('Back-end')
        javascript = Event.create_event('javascript class', category, date=None, place='Florianópolis')  # noqa:E501
        response = client.get(reverse('schedule:details', kwargs={'id': 1}))

        self.assertEqual(response.context['event'], javascript)

    def test_display_event_url_is_correct(self):
        url = reverse('schedule:details', kwargs={'id': 1})
        self.assertEqual(url, '/events/1/')

    def test_event_model_string_representation_is_name(self):
        category = Category.create_class('Back-end')
        javascript = Event.create_event('javascript class', category, date=None, place='Florianópolis')  # noqa:E501

        self.assertEqual(str(javascript), javascript.name)

    def test_event_display_uses_correct_view_function(self):
        view = resolve(reverse('schedule:details', kwargs={'id': 1}))
        self.assertEqual(view.func, display_event)

    def test_event_model_name_max_length_is_255(self):
        category = Category.create_class('Back-end')
        javascript = Event.create_event('javascript class', category, date=None, place='Florianópolis')  # noqa:E501

        javascript.name = 'A' * 256
        with self.assertRaises(ValidationError):
            javascript.full_clean()


class TestListingCategories(TestCase):
    def test_template_list_categories(self):
        back = Category.create_class('Back-end')
        mobile = Category.create_class('Mobile', active=False)
        front = Category.create_class('Front-end')

        client = Client()
        response = client.get('/categories/')

        self.assertEqual(list(response.context['categories']), [back, front])

    def test_template_used_list_categories(self):
        mobile = Category.create_class('Mobile', active=False)
        front = Category.create_class('Front-end')

        client = Client()
        response = client.get('/categories/')

        self.assertTemplateUsed(response, 'schedule/categories/listing_categories.html')  # noqa:E501

    def test_return_404_if_dont_exist_categories(self):
        client = Client()
        response = client.get('/categories/')

        self.assertEqual(response.status_code, 404)

    def test_categories_view_function_is_correct(self):
        view = resolve(reverse('schedule:categories'))

        self.assertIs(view.func, list_category)

    def test_listing_categories_url_is_correct(self):
        url = reverse('schedule:categories')
        self.assertEqual(url, '/categories/')


class TestDisplayCategory(TestCase):
    def test_template_display_category(self):
        back = Category.create_class('Back-end')
        client = Client()
        response = client.get(reverse('schedule:category_datails', kwargs={'id': 1}))  # noqa:E501

        self.assertTemplateUsed(
            response, 'schedule/categories/display_category.html')

    def test_category_specific_template_dont_loadd_category_not_active(self):
        mobile = Category.create_class('Mobile', active=False)

        client = Client()
        response = client.get(reverse('schedule:category_datails', kwargs={'id': 1}))  # noqa:E501
        self.assertEqual(response.status_code, 404)

    def test_category_specific_template_load_correct_category(self):
        mobile = Category.create_class('Mobile')

        client = Client()
        response = client.get(reverse('schedule:category_datails', kwargs={'id': mobile.id}))  # noqa:E501

        content = response.content.decode('utf-8')

        self.assertIn('Mobile', content)
        self.assertTemplateUsed(response, 'schedule/categories/display_category.html')  # noqa:E501

    def test_category_specific_url_is_correct(self):
        mobile = Category.create_class('Mobile')
        url = reverse('schedule:category_datails', kwargs={'id': 1})
        self.assertEqual(url, '/category/1/')

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('schedule:category_datails', kwargs={'id': 1}))
        self.assertEqual(view.func, category_datails)

    def test_category_model_name_max_length_is_255_chars(self):
        back = Category.create_class('Back-end')
        back.name = 'A' * 256
        with self.assertRaises(ValidationError):
            back.full_clean()

    def test_category_model_string_representation_is_name_field(self):
        mobile = Category.create_class('Mobile')
        self.assertEqual(str(mobile), mobile.name)
