from django.shortcuts import render
from .models import Image
from django.shortcuts import get_object_or_404
from django.db.models import F

def image_list(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'Image_upload/image_list.html', context)

def image_page(request, pk):
    image = get_object_or_404(Image, pk=pk)
    Image.objects.filter(pk=image.pk).update(views=F('views') + 1)
    context = {'image': image}
    return render(request, 'Image_upload/image_page.html', context)