from django.db import models
from isbn_field import ISBNField

from .validators import ratings_validator


def zero_division_handling(func):
	def wrapper_function(*agrs, **kwargs):
		try:
			return func(*agrs, **kwargs)
		except ZeroDivisionError:
			return "--"
	return wrapper_function

class Author(models.Model):
	"""
		
	"""

	name 			= models.CharField(max_length=100, unique=True)

	def __str__(self):
		return f"{self.name.title()}"

	def save(self, *args, **kwargs):
		self.name = self.name.lower()		
		super(Author, self).save(*args, **kwargs)


class Book(models.Model):
	"""

	"""

	title 			= models.CharField(max_length=100) 
	genre 			= models.CharField(max_length=30)
	ISBN 			= ISBNField(unique=True)
	author 			= models.ForeignKey(Author ,on_delete=models.SET_NULL, null=True, default=None) 

	def __str__(self):
		return f"{self.title}- {self.ISBN}"
	
	@property
	@zero_division_handling
	def general_rating(self):
		book = Book.objects.get(pk=self.pk)
		total_rates = 0
		for op in book.opinions.all():
			total_rates += op.rating
		total_rates = round(total_rates/ book.opinions.all().count(), 1)
		return total_rates

	def print_whole(self):
		for i in Book.objects.all():
			print(i.title)
		return None

	class Meta:
		ordering = ["pk"]

class Opinion(models.Model):
	"""

	"""
	description 	= models.CharField(max_length=500)
	rating 			= models.IntegerField(validators=[ratings_validator,], default=None)
	book 			= models.ForeignKey(Book, on_delete=models.CASCADE, default=None, related_name="opinions")

	def __str__(self):
		return f"{self.book.ISBN}- {self.rating}"		

	@property   
	def book_isbn(self):
		book = Book.objects.get(pk=self.pk)
		return book.ISBN

	class Meta:
		ordering = ["book"]
