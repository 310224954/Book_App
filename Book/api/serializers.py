from rest_framework import serializers

from Book.models import Book, Author, Opinion


class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Author
		fields = ("name",)


class OpinionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Opinion
		fields = ("description", "rating", "book", "book_isbn")


class BookSerializer(serializers.ModelSerializer):

	author = AuthorSerializer(read_only=True, many=False)
	opinions = OpinionSerializer(read_only=True, many=True)	

	class Meta:
		model = Book
		fields = ("title", "genre", "ISBN", "author", "opinions")



