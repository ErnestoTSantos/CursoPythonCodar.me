from django.urls import path

from .views import HoraryList, ProviderList, SchedulingDetail, SchedulingList

urlpatterns = [
    path('scheduling/', SchedulingList.as_view()),
    path('scheduling/<int:id>/', SchedulingDetail.as_view()),
    path('horary/<str:date>/', HoraryList.as_view()),
    path('providers/', ProviderList.as_view())
]
