from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view

from pilots.models import Pilot
from pilots.serializers import PilotSerializer


@api_view(http_method_names=['GET', 'POST'])
def pilots_list(request):

    if request.method == 'GET':
        qs = get_list_or_404(Pilot.objects.filter(retired=False).order_by('number'))  # noqa:E501
        serializer = PilotSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = request.data
        serializer = PilotSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def pilot_details(request, name):
    obj = get_object_or_404(Pilot, name=name.title(), retired=False)  # noqa:E501
    if request.method == 'GET':
        serializer = PilotSerializer(obj)

        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        serializer = PilotSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        obj.retired = True
        obj.save()

        serializer = PilotSerializer(obj)

        return JsonResponse(serializer.data, status=204)
