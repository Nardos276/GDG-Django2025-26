from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author


# READ (List all books)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


# READ (Single book)
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})


# CREATE
def create_book(request):

    if request.method == "POST":

        title = request.POST.get('title')
        author_id = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')

        author = Author.objects.get(id=author_id)

        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn
        )

        return redirect('book_list')

    authors = Author.objects.all()
    return render(request, 'books/book_form.html', {'authors': authors})


# UPDATE
def update_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == "POST":

        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.isbn = request.POST.get('isbn')

        book.save()

        return redirect('book_list')

    authors = Author.objects.all()

    return render(request, 'books/book_form.html', {
        'book': book,
        'authors': authors
    })


# DELETE
def delete_book(request, id):

    book = get_object_or_404(Book, id=id)
    book.delete()

    return redirect('book_list')
from django.http import JsonResponse
import json


# GET all books, POST create book
def api_books(request):

    if request.method == "GET":

        books = list(Book.objects.values(
            'id',
            'title',
            'author_id',
            'published_date',
            'isbn'
        ))

        return JsonResponse(books, safe=False)


    if request.method == "POST":

        data = json.loads(request.body)

        book = Book.objects.create(
            title=data['title'],
            author_id=data['author'],
            published_date=data['published_date'],
            isbn=data['isbn']
        )

        return JsonResponse({
            "message": "Book created",
            "id": book.id
        })


# GET one, PUT update, DELETE
def api_book_detail(request, id):

    book = get_object_or_404(Book, id=id)


    if request.method == "GET":

        data = {
            "id": book.id,
            "title": book.title,
            "author": book.author.name,
            "published_date": book.published_date,
            "isbn": book.isbn
        }

        return JsonResponse(data)


    if request.method == "PUT":

        data = json.loads(request.body)

        book.title = data['title']
        book.author_id = data['author']
        book.published_date = data['published_date']
        book.isbn = data['isbn']

        book.save()

        return JsonResponse({"message": "updated"})


    if request.method == "DELETE":

        book.delete()

        return JsonResponse({"message": "deleted"})
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer


@api_view(['GET'])
def rest_books(request):

    books = Book.objects.all()

    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)

