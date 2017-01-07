from django.shortcuts import render
from django.views.generic import View

from .models import Book, Author


# Create your views here.
def list_books(request):
    """
    List the books that have reviews
    :param request:
    :return:
    """

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
    }
    return render(request, "list.html", context)


class AuthorList(View):

    def get(self, request):

        authors = Author.objects.all()

        context = {
            'authors': authors,
        }

        return render(request, "authors.html", context)

