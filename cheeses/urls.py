from django.urls import path
# import from project
from .import views


app_name = "cheeses"

urlpatterns = [
	path(route='', view=views.CheeseListView.as_view(), name='list'),
	path(route='<slug:slug>/', view=views.CheeseDetailView.as_view(), name='detail'),
]