from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.full_report, name='report'),

    path('ticket/<str:pk>/', views.ticket_report, name='ticket')
]
