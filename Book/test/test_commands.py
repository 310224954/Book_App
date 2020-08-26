from django.test import TestCase
from django.core.management import call_command
import os

from Book.models import Book, Opinion


class TestCommand(TestCase):
	"""
		Test class prepared for testing new custom managing commands.
		Test requires preparing two input files and placing them
		in 'files' folder inside test directory
	"""

	def __init__(self, *args, **kwargs):
		#getting constants => file paths for test input files		
		self.books_test_file_path 		= __file__.replace("test_commands.py", r"files\ksiazki.txt")
		self.opinions_test_file_path 	= __file__.replace("test_commands.py", r"files\opinie.txt")
		super(TestCommand, self).__init__(*args, **kwargs)

	def setUp(self):
		call_command("import_books", self.books_test_file_path)
		call_command("import_opinions", self.opinions_test_file_path)
		self.book_1 = Book.objects.get(pk=1)
		self.opinion = Opinion.objects.get(pk=1)

	def test_import_books_command(self):		
		self.assertEqual(Book.objects.all().count(), 6)
		self.assertEqual(self.book_1.ISBN, "9788366436572")
		self.assertEqual(self.book_1.genre, "Kryminał")
		self.assertEqual(self.book_1.general_rating, 3.2)

	def test_import_opinions_command(self):
		self.assertEqual(Opinion.objects.all().count(), 11)
		self.assertEqual(Opinion.objects.filter(book=self.book_1).count(), 4)
		self.assertEqual(self.opinion.ISBN, "9788366436572")
		self.assertEqual(self.opinion.description, "test1")



