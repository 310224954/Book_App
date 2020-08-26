from django.test import TestCase
from django.urls import reverse, resolve

from Book.api.views import BookListAPI

class TestApi(TestCase):
	

	def test_search_prod_url(self):
		url = reverse("api:book_list")
		self.assertEquals(resolve(url).func.view_class, BookListAPI)
