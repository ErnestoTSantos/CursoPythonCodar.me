from django.urls import path

from .views import PilotDetails, PilotsList

urlpatterns = [
    path('', PilotsList.as_view()),
    path('<str:name>/', PilotDetails.as_view()),
]
