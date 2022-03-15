from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from schedule.serializers import SchedulingSerializer

from .models import Scheduling


@api_view(http_method_names=['GET', 'POST'])
def scheduling_list(request):
    if request.method == 'GET':
        qs = Scheduling.objects.all()
        serializer = SchedulingSerializer(qs, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = request.data
        serializer = SchedulingSerializer(data=data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            Scheduling.objects.create(
                date_time=validated_data['date_time'],
                client_name=validated_data['client_name'],
                client_email=validated_data['client_email'],
                client_phone=validated_data['client_phone'],
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# Aqui a view irá ser vista como uma api e sempre retornará elementos json.
# Atualmente recebe apenas o método GET.
@api_view(http_method_names=['GET'])
def scheduling_detail(request, id):
    obj = get_object_or_404(Scheduling, id=id)
    serializer = SchedulingSerializer(obj)

    return JsonResponse(serializer.data)
