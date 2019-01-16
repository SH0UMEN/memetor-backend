from django.urls import path
from . import views

urlpatterns = [
    path('all-images', views.allImages),
    path('create-mem', views.createMem)
]
