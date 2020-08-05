from django.urls import path
# Import from project
from .views import index

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
]
