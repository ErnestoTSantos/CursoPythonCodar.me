from django.urls import path

from schedule.views import (category_datails, display_event, list_category,
                            list_events, participate_event)

app_name = 'schedule'

urlpatterns = [
    path('events/', list_events, name='index'),
    path('events/<int:id>/', display_event, name='details'),
    path('participate/', participate_event, name='participate_event'),
    path('categories/', list_category, name='categories'),
    path('category/<int:id>/', category_datails, name='category_datails')
]
