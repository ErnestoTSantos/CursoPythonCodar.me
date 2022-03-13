from django.urls import path

from accommodations.views import (accommodation, accommodation_details,
                                  company, company_details,
                                  create_accommodation, create_company,
                                  list_accommodations, list_companies)

app_name = 'accommodation'

urlpatterns = [
    path('', list_accommodations, name='source'),  # noqa:E501
    path('api/accommodations_list/', list_accommodations, name='accommodations'),  # noqa:E501
    path('api/accommodation_details/<str:accommodation_name>/', accommodation_details, name='accommodation_details'),  # noqa:E501
    path('api/companies_list/', list_companies, name='companies'),
    path('api/company_details/<str:name>/', company_details, name='company_details'),  # noqa:E501
    path('company/', company, name='company'),
    path('accommodation/<str:company>/', accommodation, name='accommodation'),  # noqa:E501
    path('create_accommodation/', create_accommodation, name='create_accommodation'),  # noqa:E501
    path('create_company/', create_company, name='create_company'),
]
