from accommodations.models import Accommodation, Company
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from reserve.models import Reserve


def reserve(request, company, accommodation):
    company_object = get_object_or_404(Company, name=company)  # noqa:E501
    accommodation_object = get_object_or_404(Accommodation, accommodation_name=accommodation)  # noqa:E501

    return render(
        request,
        'reserve/create_reserve.html',
        {
            'accommodation': accommodation_object,
            'company': company_object
        }
    )


def create_reserve(request):
    accommodation = get_object_or_404(Accommodation, accommodation_name=request.POST.get('accommodation'))  # noqa:E501
    try:
        check_in = request.POST.get('check-in')
        check_out = request.POST.get('check-out')
        people = request.POST.get('people')
        person = request.POST.get('person')

        accommodation.times_rented += 1
        accommodation.save()

        Reserve.create_reservation(accommodation=accommodation, check_in=check_in, check_out=check_out, person=person, amount_people=people)  # noqa:E501

    except ValueError as error:
        print(error)

    return redirect('reserve:reserve', accommodation.company.name, accommodation.accommodation_name)  # noqa:E501


def verify_reserve(request, person):
    reserve_detail = get_object_or_404(Reserve, person=person)

    informations_dict = {
        'Responsible': reserve_detail.person,
        'Accommodation': reserve_detail.accommodation.accommodation_name,
        'Check-in': reserve_detail.check_in,
        'Check-out': reserve_detail.check_out,
        'Amount of people': reserve_detail.amount_people,
        'Accommodation informations': f'http://127.0.0.1:8000/api/accommodation_details/{reserve_detail.accommodation.accommodation_name}/'
    }

    return JsonResponse(data=informations_dict)
