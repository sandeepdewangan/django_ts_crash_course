from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


# TimeStampedModel automatically gives the model created and modified fields, 
# which automatically track when the object is created or modified.

class Cheese(TimeStampedModel):

	# Choices selection
	class Firmness(models.TextChoices):
		UNSPECIFIED = "unspecified", "Unspecified"
		SOFT = "soft", "Soft"
		SEMI_SOFT = "semi-soft", "Semi Soft"
		HARD = "hard", "Hard"


	name = models.CharField("Name of Cheese", max_length=255)
	slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
	description = models.TextField("Description", blank=True)
	firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)


	def __str__(self):
		return self.name