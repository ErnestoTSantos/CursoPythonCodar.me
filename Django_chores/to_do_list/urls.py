from django.urls import path

from to_do_list.views import display_chore, listing_chores

app_name = 'chores'

urlpatterns = [
    path('chores_list/<str:author>/', listing_chores, name='listing_chores'),
    path('chores_list/<str:author>/<int:id>/',
         display_chore, name='chore_detailing'),
]
