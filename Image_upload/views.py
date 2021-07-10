from django.shortcuts import render
from .models import Image
from django.utils import timezone

def image_list(request):
    images = Image.objects.all()
    return render(request, 'Image_upload/image_list.html', {'images': images})
