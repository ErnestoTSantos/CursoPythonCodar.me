from datetime import date

# from django.http import JsonResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from schedule.models import Category, Event


def list_events(request):
    today_date = date.today()
    events = Event.objects.exclude(date__lt=today_date).order_by('date')
    categories = Category.objects.all()

    # events_dict = {}

    # for event in events:
    #     events_dict[event.name] = {
    #         'name': event.name,
    #         'category': event.category.name,
    #         'place': event.place,
    #         'link': event.link,
    #         'participants': event.participants
    #     }

    return render(
        request,
        'schedule/events/listing_events.html',
        {
            'events': events,
            'toDefine': 'A definir',
            'categories': categories,
        }
    )

    # Retorna o elemento no formato JSON
    # return JsonResponse(data=events_dict)


def display_event(request, id):
    event = get_object_or_404(Event, id=id)

    return render(
        request,
        'schedule/events/display_event.html',
        {'event': event}
    )


def participate_event(request):
    event_id = request.POST.get('event_id')
    event = get_object_or_404(Event, id=event_id)

    event.participants += 1
    event.save()

    return redirect('schedule:details', event.id)


def list_category(request):
    # categories = Category.objects.filter(active=True).order_by('name')
    categories = get_list_or_404(Category.objects.filter(active=True).order_by('name'))  # noqa:E501

    return render(
        request,
        'schedule/categories/listing_categories.html',
        {
            'categories': categories
        }
    )


def category_datails(request, id):
    category = get_object_or_404(Category, id=id, active=True)

    events = Event.objects.filter(category=category)

    events_amount = events.count()

    return render(
        request,
        'schedule/categories/display_category.html',
        {
            'category': category,
            'amount': events_amount,
        }
    )


def create_category(request):
    try:
        category_name = request.POST.get('category_name')
        category_description = request.POST.get('category_description')
        if category_description:
            Category.create_class(name=category_name,
                                  description=category_description)
        else:
            Category.create_class(name=category_name)

    except ValueError as error:
        print(error)

    return redirect('schedule:categories')


def create_event(request):
    try:
        event_name = request.POST.get('event_name')
        category_name = request.POST.get('category')
        event_date = str(request.POST.get('date'))
        place = request.POST.get('place')
        link = request.POST.get('link')

        if not place:
            place = None

        if not link:
            link = None

        if not category_name:
            raise ValueError('Você precisa selecionar uma categoria!')

        if not event_date:
            event_date = None

        category_object = get_object_or_404(Category, name=category_name)

        Event.create_event(name=event_name, category=category_object, date=event_date, link=link, place=place)  # noqa:E501
    except ValueError as error:
        print(error)

    return redirect('schedule:index')
