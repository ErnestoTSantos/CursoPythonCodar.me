from django.urls import path

from .views import CategoriesList, CategoryDetails, CategoryPilotsList

urlpatterns = [
    path("", CategoriesList.as_view()),
    path("details/<str:name>/", CategoryDetails.as_view()),
    path("categoryPilots/", CategoryPilotsList.as_view()),
]
