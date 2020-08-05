from django.db import models
from django.urls import reverse
from django.conf import settings
# Third Party Packages
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django_countries.fields import CountryField




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
	country_of_origin = CountryField("Country of Origin", blank=True)
	creater = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

	def get_absolute_url(self):
		"""
			This can be used to redirect user from cheese add page to detail page. 
			Then we need not to define success_url in CheeseCreateView view.
			Return absolute URL to the Cheese Detail page.
		"""
		return reverse('cheeses:detail', kwargs={"slug": self.slug})

	def __str__(self):
		return self.name