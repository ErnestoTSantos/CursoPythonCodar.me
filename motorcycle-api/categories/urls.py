from django.urls import path

from .views import categories_list, category_details

urlpatterns = [
    path('', categories_list),
    path('<str:name>/', category_details)
]
