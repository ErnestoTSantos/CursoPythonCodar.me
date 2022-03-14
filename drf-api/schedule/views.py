from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from schedule.serializers import SchedulingSerializer

from .models import Scheduling


@api_view(http_method_names=['GET'])
def scheduling_list(request):
    qs = Scheduling.objects.all()
    serializer = SchedulingSerializer(qs, many=True)

    return JsonResponse(serializer.data, safe=False)


# Aqui a view irá ser vista como uma api e sempre retornará elementos json.
# Atualmente recebe apenas o método GET.
@api_view(http_method_names=['GET'])
def scheduling_detail(request, id):
    obj = get_object_or_404(Scheduling, id=id)
    serializer = SchedulingSerializer(obj)

    return JsonResponse(serializer.data)
