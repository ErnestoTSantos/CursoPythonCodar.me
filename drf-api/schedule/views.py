from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from schedule.serializers import ProviderSerializer, SchedulingSerializer

from .models import Scheduling


class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        username = request.query_params.get('username', None)
        if request.user.username == username:
            return True
        return False


class IsProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.provider == request.user:
            return True
        return False


class SchedulingList(generics.ListCreateAPIView):  # noqa:E501

    serializer_class = SchedulingSerializer
    permission_classes = [IsOwnerOrCreateOnly]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        queryset = Scheduling.objects.filter(provider__username=username, canceled=False)  # noqa:E501
        return queryset


class SchedulingDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsProvider]
    queryset = Scheduling.objects.filter(canceled=False)
    serializer_class = SchedulingSerializer
    lookup_field = 'id'

    def perform_destroy(self, instance):
        instance.canceled = True
        instance.save()

        return Response(status=204)


class ProviderList(generics.ListAPIView):  # noqa:E501
    serializer_class = ProviderSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.IsAdminUser]


class HoraryList(APIView):
    def get(self, request, date):
        username = request.query_params.get('username', None)
        obj = User.objects.filter(username=username)
        if obj:
            date = datetime.strptime(date, '%Y-%m-%d').date()

            qs = Scheduling.objects.filter(canceled=False, date_time__date=date, provider__username=username).order_by('date_time__time')  # noqa:E501
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
        return Response(status=404)
