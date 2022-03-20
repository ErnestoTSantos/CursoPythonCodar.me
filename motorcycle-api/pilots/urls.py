from django.urls import path

from .views import pilot_details, pilots_list

urlpatterns = [
    path('', pilots_list),
    path('<str:name>/', pilot_details),
]
