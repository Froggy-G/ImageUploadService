from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:pk>', views.image_page, name='image_page'),
    path('image/new', views.image_new, name='image_new'),
    path('image/<pk>/remove/', views.image_remove, name='image_remove'),
    path('registration/', views.registration, name='registration'),
    path('registration_done/', views.registration_done, name='registration_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)