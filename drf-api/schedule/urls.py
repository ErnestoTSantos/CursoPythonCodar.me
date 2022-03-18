from django.urls import path

from .views import horary_list, scheduling_detail, scheduling_list

urlpatterns = [
    path('scheduling/', scheduling_list),
    path('scheduling/<int:id>/', scheduling_detail),
    path('horary/<str:date>/', horary_list)
]
