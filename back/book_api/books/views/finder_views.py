from rest_framework.response import Response
from rest_framework.views import APIView
from unidecode import unidecode

from ..models import Books
from ..serializers import BookSerializer


class BooksFinderBase(APIView):
    def get_books_by_key(self, value, key):
        normalized_value = unidecode(value.lower())
        books = [book for book in Books.objects.all() if normalized_value == unidecode(
            getattr(getattr(book, key), key).lower())]
        books_serialized = BookSerializer(books, many=True)

        return books_serialized.data


class BooksByAuthor(BooksFinderBase):
    def get(self, request, author):
        books = self.get_books_by_key(author, 'autor')

        return Response(books)


class BooksByCategory(BooksFinderBase):
    def get(self, request, category):
        books = self.get_books_by_key(category, 'categoria')

        return Response(books)


class BooksByPublisher(BooksFinderBase):
    def get(self, request, publisher):
        books = self.get_books_by_key(publisher, 'editorial')

        return Response(books)


class AuthorsByCategory(BooksFinderBase):
    def get(self, request, category):
        books = self.get_books_by_key(category, 'categoria')

        return Response(books)
