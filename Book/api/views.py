from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from Book.models import Book
from .serializers import BookSerializer


class BookListAPI(ListAPIView):
	queryset 			= Book.objects.all()
	serializer_class 	= BookSerializer
	search_fields 		= ("title",)
	filter_backends 	= (SearchFilter, OrderingFilter,)
	pagination_class 	= PageNumberPagination
