from django.core.exceptions import ValidationError

def ratings_validator(value):
	#Checks whether the issued raiting is within the acceptbale range
	if value < 0:
		raise ValidationError(
			(f"Worst rate you can choose for book is 1, you cannot rate below that."),
			params={"value": value},
		)
	elif value > 6:
		raise ValidationError(
			(f"Highest possible rating for book is 6, please choose any value between 1 and 6."),
			params={"value": value},
		)
		