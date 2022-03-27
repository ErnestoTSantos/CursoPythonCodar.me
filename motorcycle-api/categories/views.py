from rest_framework import generics, permissions
from rest_framework.response import Response

from categories.models import Category
from categories.serializers import CategoryPilotsSerializer, CategorySerializer


class CategoriesList(generics.ListCreateAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.filter(active=True)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.filter(active=True)
    lookup_field = 'name'

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
        return Response(status=204)


class CategoryPilotsList(generics.ListAPIView):

    serializer_class = CategoryPilotsSerializer
    queryset = Category.objects.filter(active=True)

    permission_classes = [permissions.IsAdminUser]
