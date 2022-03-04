from datetime import date

# from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from schedule.models import Category, Event


def list_events(request):
    today_date = date.today()
    events = Event.objects.filter(date__gte=today_date).order_by('date')

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
            'toDefine': 'A definir'
        }
    )

    # Retorna o elemento no formato JSON
    # return JsonResponse(data=events_dict)


def display_event(request, id):
    today_date = date.today()
    event = get_object_or_404(Event, id=id, date__gte=today_date)

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
    categories = Category.objects.all().order_by('?')

    return render(
        request,
        'schedule/categories/listing_categories.html',
        {
            'categories': categories
        }
    )


def category_datails(request, id):
    category = get_object_or_404(Category, id=id)

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
