from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
     path('obituary_form', views.obituary_form, name="obituary_form"),
]