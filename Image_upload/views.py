from django.shortcuts import render
from .models import Image
from django.shortcuts import get_object_or_404

def image_list(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'Image_upload/image_list.html', context)

def image_page(request, pk):
    image = get_object_or_404(Image, pk=pk)
    context = {'image': image}
    return render(request, 'Image_upload/image_page.html', context)