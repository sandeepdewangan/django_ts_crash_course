from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# import from project
from .models import Cheese


class CheeseListView(ListView):
	model = Cheese


class CheeseDetailView(DetailView):
	model = Cheese
	template_name = "cheeses/my_cheese_detail.html"
	context_object_name = 'mycheese'


class CheeseCreateView(LoginRequiredMixin, CreateView):
	model = Cheese
	fields = ['name', 'description', 'firmness', 'country_of_origin', ]
	template_name = "cheeses/add.html"

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)


class CheeseUpdateView(LoginRequiredMixin, UpdateView):
	model = Cheese
	fields = ['name', 'description', 'firmness', 'country_of_origin']
	action = 'Update'
	template_name = "cheeses/add.html"
