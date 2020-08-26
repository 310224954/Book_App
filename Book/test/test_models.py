from django.test import TestCase
from Book.models import Opinion, Book, Author

class TestModels(TestCase):
	"""
		Test class preapred for testing models and relations between them. 
	"""
	def setUp(self):
		self.author_1 		= Author.objects.create(name="Jan Kowalski")
		self.author_2 		= Author.objects.create(name="John Smith")
		self.author_3 		= Author.objects.create(name="Test testowy")

		self.book_1 		= Book.objects.create(
								title="test",
								genre="test_genre",
								ISBN="9780553386790",
								author=self.author_1
							)

		self.opinion_1		 = Opinion.objects.create(
								description="Not bad, not bad",
								rating=3,
								book=self.book_1,
								)
		self.opinion_2 		= Opinion.objects.create(
								description="Completely trash book",
								rating=1,
								book=self.book_1,
								)
		self.opinion_3 		= Opinion.objects.create(
								description="Very good story book",
								rating=5,
								book=self.book_1,
								)

	def test_author_model(self):
		self.assertEqual(self.author_1.name, "jan kowalski")
		self.assertEqual(self.author_1.__str__(), "Jan Kowalski")

	def test_book_model(self):
		self.assertEqual(self.book_1.ISBN, "9780553386790")
		self.assertEqual(self.book_1.opinions.all().count(), 3)
		self.assertEqual(self.book_1.general_rating, 3.0)

		self.opinion_4 		= Opinion.objects.create(
								description="Very good story book",
								rating=3,
								book=self.book_1,
							)		
		self.assertEqual(self.book_1.opinions.all().count(), 4)
		self.assertEqual(self.book_1.general_rating, 3.0)

	def test_opiion_model(self):
		self.assertEqual(self.opinion_1.ISBN, self.book_1.ISBN)		
