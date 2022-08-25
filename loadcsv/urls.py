from django.urls import path
# from .views import upload_file_view
from . import views

# app_name = 'loadcsv'

urlpatterns = [
    path('', views.upload_file_view, name='uploadcsv'),
]

