from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("author", views.author),
    path("book", views.book),
    path("authors/<a_id>", views.author_view),
    path("books/<b_id>", views.book_view),
    path("author_view", views.author_view),
    path("book_view", views.book_view),
    path("add_book_to_author", views.add_book_to_author),
    path("add_author_to_book", views.add_author_to_book),
    path("add_author", views.add_authors),
    path("add_book", views.add_books),
]
