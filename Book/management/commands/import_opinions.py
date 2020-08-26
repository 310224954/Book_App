from django.core.management.base import BaseCommand, CommandError
import csv

from Book.models import Book, Opinion

class Command(BaseCommand):
	help = "Creates Opinion class objects in database based on csv file input."

	def add_arguments(self, parser):
		parser.add_argument("path", type=str, help="file path")

	def handle(self, *args, **options):
		file_path = options["path"]
		with open(file_path, "r", encoding="UTF-8") as csv_file:
			reader = csv.reader(csv_file, delimiter=';')
			next(reader) #skipping headers
			for line in reader:
				book = Book.objects.get(ISBN=line[0])
				new_opinion = Opinion(
							description=line[2],
							rating=line[1],
							book=book
					)
				new_opinion.save()
				