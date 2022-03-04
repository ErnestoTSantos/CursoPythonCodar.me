from django.shortcuts import get_object_or_404, redirect, render
from to_do_list.models import Chore

from authors.models import Author


def list_authors(request):
    authors = Author.objects.all().order_by('first_name')

    return render(
        request,
        'authors/list_authors.html',
        {
            'authors': authors,
        }
    )


def author_description(request, first_name):
    author = get_object_or_404(Author, first_name=first_name)

    chores = Chore.objects.filter(author=author)

    amount_chores = chores.count()

    return render(
        request,
        'authors/author_details.html',
        {
            'author': author,
            'amount': amount_chores,
        }
    )


def create_chore(request):
    author_first_name = request.POST.get('author_name')
    author = get_object_or_404(Author, first_name=author_first_name)
    chore_name = request.POST.get('chore_name')
    active_chore = bool(request.POST.get('active_chore'))
    final_date = request.POST.get('finish_date')

    Chore.create_chore(author, chore_name, active_chore, final_date)

    return redirect('authors:author_details', author_first_name)


def create_author(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')

    Author.create_author(first_name=first_name, last_name=last_name, age=age)

    # Forma de capturar os erros para retornar uma página de bad request

    # try:
    #     Author.create_author(first_name=first_name,
    #                          last_name=last_name, age=age)
    # except ValueError as error:
    #     return render(request, '...', {'error': error})

    return redirect('authors:authors_list')
