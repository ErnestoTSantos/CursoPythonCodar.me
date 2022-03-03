from authors.models import Author
from django.shortcuts import get_object_or_404, render

from to_do_list.models import Chore


def listing_chores(request, author):
    query_author = get_object_or_404(Author, first_name=author)
    chores = Chore.objects.filter(
        author=query_author, active=True).order_by('create_date')

    return render(
        request,
        'to_do_list/list_chores.html',
        {
            'chores': chores,
            'author': query_author,
        }
    )


def display_chore(request, author, id):

    query_author = get_object_or_404(Author, first_name=author)
    chore_details = get_object_or_404(Chore, id=id, active=True)

    return render(
        request,
        'to_do_list/chore_datails.html',
        {
            'chore': chore_details,
            'author': query_author,
        }
    )
