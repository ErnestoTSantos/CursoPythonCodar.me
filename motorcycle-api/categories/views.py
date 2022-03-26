from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from categories.models import Category
from categories.serializers import CategorySerializer


@api_view(http_method_names=['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        qs = get_list_or_404(Category, active=True)
        serializer = CategorySerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = request.data
        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def category_details(request, name):
    obj = get_object_or_404(Category.objects.filter(name=name))
    if request.method == 'GET':
        serializer = CategorySerializer(obj)

        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        data = request.data
        serializer = CategorySerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        obj.active = False
        obj.save()

        return Response(status=204)
