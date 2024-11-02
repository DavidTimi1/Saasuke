from django.urls import path, include

from . import views

app_name = "auth"

urlpatterns = [
    path('', views.index),
    path('google-signin', views.google_signin, name="google_signin"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
