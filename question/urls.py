from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("option.urls", namespace="option")), 
    path('admin/', admin.site.urls),
]
