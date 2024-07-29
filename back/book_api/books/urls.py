from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("", views.BookView.as_view(), name="book_view"),
]
