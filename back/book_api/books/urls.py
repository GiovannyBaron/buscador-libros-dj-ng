from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("", views.BookView.as_view(), name="book_view"),
    
    path("autor/", views.Author.as_view(), name="author"),
    path("categoria/", views.Category.as_view(), name="category"),
    path("editorial/", views.Publisher.as_view(), name="publisher"),
    path("libro/", views.Book.as_view(), name="book"),

    path("libros-por-autor/<str:author>/",
         views.BooksByAuthor.as_view(), name="books_by_author"),
    path("libros-por-categoria/<str:category>/", views.BooksByCategory.as_view(),
         name="books_by_category"),
    path("libros-por-editorial/<str:publisher>/", views.BooksByPublisher.as_view(),
         name="books_by_publisher"),
    path("autores-por-categoria/<str:category>/", views.AuthorsByCategory.as_view(),
         name="authors_by_category"),
]
