from django.urls import path

from reserve.views import create_reserve, reserve, verify_reserve

app_name = 'reserve'

urlpatterns = [
    path('reserve/<str:company>/<str:accommodation>/', reserve, name='reserve'),  # noqa:E501
    path('create_reserve/', create_reserve, name='create_reserve'),  # noqa:E501
    path('api/verify_reserve/<str:person>/', verify_reserve, name='verify_reserve'),  # noqa:E501
]
