from books_authors_app.models import Book, Author
from django.shortcuts import redirect, render, HttpResponse


def index(request):
    context = {"saludo": "Hola "}
    return render(request, "index.html", context)


def author(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {"books": books, "authors": authors}
    return render(request, "authors.html", context)


def book(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {"saludo": "Hola libros", "books": books, "authors": authors}
    return render(request, "books.html", context)


def add_authors(request):
    a_nombre = request.POST["nombre"]
    a_apellido = request.POST["apellido"]
    a_notas = request.POST["notas"]
    Author.objects.create(first_name=a_nombre, last_name=a_apellido, notes=a_notas)
    return redirect("/author")


def add_books(request):
    b_titulo = request.POST["titulo"]
    b_desc = request.POST["descripcion"]
    Book.objects.create(title=b_titulo, desc=b_desc)
    return redirect("/book")


def author_view(request, a_id):
    authors = Author.objects.get(id=a_id)
    books = Book.objects.all()
    context = {"authors": authors, "books": books}
    return render(request, "authorview.html", context)


def book_view(request, b_id):
    authors = Author.objects.all()
    books = Book.objects.get(id=b_id)
    context = {"authors": authors, "books": books}
    return render(request, "bookview.html", context)


def add_book_to_author(request):
    b_id = int(request.POST["book_id"])
    a_id = int(request.POST["author_id"])
    author = Author.objects.get(id=a_id)
    book = Book.objects.get(id=b_id)
    author.books.add(book)
    return redirect(request.META.get("HTTP_REFERER"))


def add_author_to_book(request):
    b_id = int(request.POST["book_id"])
    a_id = int(request.POST["author_id"])
    author = Author.objects.get(id=a_id)
    book = Book.objects.get(id=b_id)
    book.authors.add(author)
    return redirect(request.META.get("HTTP_REFERER"))
