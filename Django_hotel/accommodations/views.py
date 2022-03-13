from django.http import JsonResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from accommodations.models import Accommodation, Company


def list_accommodations(request):
    accommodations = get_list_or_404(Accommodation)

    accommodations_dict = {}

    for accommodation in accommodations:
        accommodations_dict[accommodation.accommodation_name] = {
            'company': accommodation.company.name,
            'accommodation_name': accommodation.accommodation_name,
            'price': f'R${accommodation.price}',
            'number_of_people': accommodation.number_of_people,
            'Details': f'http://127.0.0.1:8000/api/accommodation_details/{accommodation.accommodation_name}/'  # noqa:E501
        }

    return JsonResponse(data=accommodations_dict)


def accommodation_details(request, accommodation_name):
    accommodation = get_object_or_404(Accommodation, accommodation_name=accommodation_name)  # noqa:E501

    accommodation_data = {
        'company': accommodation.company.name,
        'accommodation_name': accommodation.accommodation_name,
        'description': accommodation.description,
        'rented': accommodation.times_rented,
        'price': f'R${accommodation.price}',
        'number_of_people': accommodation.number_of_people,
        'return_to_list': 'http://127.0.0.1:8000/api/accommodations_list/'
    }

    return JsonResponse(data=accommodation_data)


def list_companies(request):
    companies = get_list_or_404(Company)

    companies_dict = []

    for company in companies:
        companies_dict.append({
            'name': company.name,
            'state': company.state,
            'address': company.address,
            'Details': f'http://127.0.0.1:8000/api/company_details/{company.name}/'  # noqa:E501
        })

    return JsonResponse(data=companies_dict, safe=False)


def company_details(request, name):
    company = get_object_or_404(Company, name=name)

    informations = []

    company_data = {
        'name': company.name,
        'since': company.since.strftime('%d/%m/%Y'),
        'description': company.description,
        'state': company.state,
        'address': company.address,
        'return to list companies': 'http://127.0.0.1:8000/api/companies_list/',  # noqa:E501
        'add a room': f'http://127.0.0.1:8000/accommodation/{company.name}'
    }

    accommodations_list = get_list_or_404(Accommodation, company=company)
    accommodation_dict = {}

    for accommodation in accommodations_list:
        accommodation_dict[accommodation.accommodation_name] = {
            'accommodation_name': accommodation.accommodation_name,
            'price': f'R${accommodation.price}',
            'number_of_people': accommodation.number_of_people,
            'Details': f'http://127.0.0.1:8000/api/accommodation_details/{accommodation.accommodation_name}/'  # noqa:E501
        }

    informations.append(company_data)
    informations.append(accommodation_dict)

    return JsonResponse(data=informations, safe=False)


def accommodation(request, company):
    company_object = get_object_or_404(Company, name=company)

    return render(
        request,
        'accommodations/create_accommodation.html',
        {'company': company_object}
    )


def company(request):
    states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará',  # noqa:E501
              'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']  # noqa:E501

    return render(request, 'company/create_company.html', {'states': states})


def create_accommodation(request):
    try:
        company = request.POST.get('company')
        name = request.POST.get('accommodation')
        description = request.POST.get('description')
        price = request.POST.get('price')
        for_number_people = request.POST.get('number_people')

        company = get_object_or_404(Company, name=company)

        Accommodation.create_accommodation(company, name, description, price, for_number_people)  # noqa:E501
    except ValueError as error:
        print(error)

    return redirect('accommodation:accommodation', company)


def create_company(request):
    try:
        name = request.POST.get('name')
        since = request.POST.get('since')
        description = request.POST.get('description')
        state = request.POST.get('state')
        address = request.POST.get('address')

        Company.create_company(name, since, description, state, address)

    except ValueError as error:
        print(error)

    return redirect('accommodation:company')
