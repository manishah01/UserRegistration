from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('make_new_user', views.make_new_user),
]