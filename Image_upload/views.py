from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Image
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def image_list(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'Image_upload/image_list.html', context)

def image_page(request, pk):
    image = get_object_or_404(Image, pk=pk)
    Image.objects.filter(pk=image.pk).update(views=F('views') + 1)
    context = {'image': image}
    return render(request, 'Image_upload/image_page.html', context)

@login_required
def image_new(request):
    if request.method == "POST":
        for file in request.FILES.getlist('images'):
            image = Image(image=file)
            image.save()
    return render(request, 'Image_upload/image_new.html', {})

@login_required
def image_remove(request, pk):
    image = get_object_or_404(Image, pk=pk)
    image.delete()
    return redirect('image_list')

def registration(request):
    user = User
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST['username']
            user.password1 = request.POST['password1']
            user.password2 = request.POST['password2']
            user.save()
            return redirect('registration_done')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {'form': form})

def registration_done(request):
    return render(request, 'registration/registration_done.html', {})