from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='Image_list')
]