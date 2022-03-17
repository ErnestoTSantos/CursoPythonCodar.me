from datetime import datetime, timedelta

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
    obj = get_object_or_404(Scheduling.objects.filter(id=id, canceled=False).order_by('date_time'))  # noqa:E501
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


@api_view(http_method_names=['GET'])
def horary_list(request, date):
    if request.method == 'GET':
        date = datetime.strptime(date, '%Y-%m-%d').date()

        qs = Scheduling.objects.filter(
            canceled=False, date_time__date=date).order_by('date_time__time')
        serializer = SchedulingSerializer(qs, many=True)

        appointment_list = []

        dt_start = datetime(date.year, date.month, date.day, 9)  # noqa:E501
        dt_end_saturday = datetime(date.year, date.month, date.day, 13)
        dt_end = datetime(date.year, date.month, date.day, 18)  # noqa:E501
        delta = timedelta(minutes=30)  # noqa:E501

        if date.weekday() != 5 and date.weekday() != 6:
            while dt_start != dt_end:

                appointment_list.append({
                    'date_time': dt_start
                })

                dt_start += delta

        if date.weekday() == 5:
            while dt_start != dt_end_saturday:
                appointment_list.append({
                    'date_time': dt_start
                })

                dt_start += delta

        if date.weekday() == 6:
            appointment_list.append({
                'Information': 'Infelizmente o estabelecimento não trabalha aos domingos!'
            })

        for element in serializer.data:
            element = element.get('date_time')
            time_element = element[11:16]
            for time in appointment_list:
                date_time = time.get('date_time')
                time_list = datetime.strftime(date_time, '%H:%M')
                if time_element == time_list:
                    appointment_list.remove(time)

        return JsonResponse(appointment_list, safe=False)
