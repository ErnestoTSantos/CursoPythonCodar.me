from django.urls import path

from assignments.views import AssignmentDetails, ListAssignments, status_check

urlpatterns = [
    path("", status_check),
    path("list_assignments/", ListAssignments.as_view()),
    path("assignment_details/<int:id>/", AssignmentDetails.as_view()),
]
