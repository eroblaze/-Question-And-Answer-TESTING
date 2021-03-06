from django.urls import path

from . import views

app_name = "option"

urlpatterns = [
    path('', views.index, name="index"),
    path('check/', views.process, name="process"),
    path('result/', views.result, name="result"),
    path('create/', views.create, name="create"),
    path('delete/', views.delete, name="delete"),
]