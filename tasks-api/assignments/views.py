from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer


class ListAssignments(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        username = self.request.user.username
        creator = self.request.query_params.get("username", None)

        queryset = []

        if username == creator:
            user = User.objects.filter(username=creator).first()
            queryset = Assignment.objects.filter(creator=user, active=True)
        elif User.objects.filter(username=username, is_staff=True).first():
            queryset = Assignment.objects.all()

        return queryset


class AssignmentDetails(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssignmentSerializer
    lookup_field = "id"
    queryset = Assignment.objects.all()


@api_view(http_method_names=["GET"])
def status_check(request):
    return Response({"status": "OK"}, status=200)
