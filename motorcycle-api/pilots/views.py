from rest_framework import generics, permissions
from rest_framework.response import Response

from pilots.models import Pilot
from pilots.serializers import PilotSerializer


class PilotsList(generics.ListCreateAPIView):

    serializer_class = PilotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pilot.objects.filter(retired=False)


class PilotDetails(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pilot.objects.filter(retired=False)
    serializer_class = PilotSerializer
    lookup_field = "name"

    def perform_destroy(self, instance):
        instance.retired = True
        instance.save()
        return Response(status=204)
