from django.urls import path
from . import views

app_name = "feedback"

urlpatterns = [
    path('', views.index),
    path('<str:app_name>', views.feedback),
]