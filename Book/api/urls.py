from django.urls import path

from .views import BookListAPI

app_name = "api"

urlpatterns = [
	path("book_list/", BookListAPI.as_view(), name="book_list"),
]
