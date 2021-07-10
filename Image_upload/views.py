from django.shortcuts import render

def image_list(request):
    return render(request, 'Image_upload/image_list.html', {})
