from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from schedule.serializers import SchedulingSerializer

from .models import Scheduling


@api_view(http_method_names=['GET', 'POST'])
def scheduling_list(request):
    if request.method == 'GET':
        qs = get_list_or_404(Scheduling, canceled=False)
        serializer = SchedulingSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = request.data
        serializer = SchedulingSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# Aqui a view irá ser vista como uma api e sempre retornará elementos json.
# Atualmente recebe os métodos GET e PATCH.
@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def scheduling_detail(request, id):
    obj = get_object_or_404(Scheduling, id=id, canceled=False)
    if request.method == 'GET':
        serializer = SchedulingSerializer(obj)

        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        # Permissão de fazer modificações únicas, sem precisar do corpo todo.
        serializer = SchedulingSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        obj.canceled = True
        obj.save()

        # O código 204 demonstra que foi bem sucedida
        return Response(status=204)
