from django.shortcuts import render
from django.views.generic import ListView, DetailView
# import from project
from .models import Cheese


class CheeseListView(ListView):
	model = Cheese


class CheeseDetailView(DetailView):
	model = Cheese
	template_name = "cheeses/my_cheese_detail.html"
	context_object_name = 'mycheese'