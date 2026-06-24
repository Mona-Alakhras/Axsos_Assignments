from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_book',views.add_book),
    path('books/<int:book_id>',views.book_details),
    path('books/<int:book_id>/add_author',views.add_author_to_book),
    path('authors', views.authors_index),
    path('add_author',views.add_author),
    path('authors/<int:author_id>',views.author_details),
    path('authors/<int:author_id>/add_book',views.add_book_to_author),
]