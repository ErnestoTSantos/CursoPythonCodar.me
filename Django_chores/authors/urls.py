from django.urls import path

from authors.views import (author_description, create_author, create_chore,
                           list_authors)

app_name = 'authors'

urlpatterns = [
    path('authors_list/', list_authors, name='authors_list'),
    path('author_details/<str:first_name>/', author_description, name='author_details'),  # noqa:E501
    path('create_chore/', create_chore, name='creating_chore'),
    path('create_author/', create_author, name='creating_author'),
]
