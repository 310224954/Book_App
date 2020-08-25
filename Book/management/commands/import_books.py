from django.core.management.base import BaseCommand, CommandError
import csv

from Book.models import Book, Opinion, Author

class Command(BaseCommand):
	help = "Loads data from csv file into database."

	def add_arguments(self, parser):
		parser.add_argument("path", type=str, help="file path")

	def handle(self, *args, **options):
		file_path = options["path"]
		with open(file_path, "r", encoding="UTF-8") as csv_file:
			reader = csv.reader(csv_file, delimiter=';')
			next(reader)
			for line in reader:
				author, status = Author.objects.get_or_create(name=line[2].lower())
				if status:			
					author.save()
				new_book = Book(
							title=line[1],
							genre=line[3],
							ISBN=line[0],
							author = author
					)
				new_book.save()