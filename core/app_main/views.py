from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PictureForm
from .models import Picture

# Create your views here.
def main(request):
    return render(request, "app_main/index.html", context={"title": "app_main"})

def upload(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            form.save()
            return redirect(to="app_main:pictures")

    form = PictureForm(instance=Picture()) # bind Picture-model to PictureForm
    return render(request, "app_main/upload.html", context={"title": "upload image", "form": form})

def pictures(request):
    imgs = Picture.objects.all()
    return render(request, "app_main/pictures.html", 
                  context={"title": "pictures output", "pictures": imgs, "media":settings.MEDIA_URL})

def remove(request):
    pass


def edit(request, pic_id):
    # <input type="text" class="form-control" value="{{pic.description}}" name="description">
    if request.method == 'POST':
        description = request.POST.get('description')
        picture = Picture.objects.filter(pk=pic_id).update(description=description)
        return redirect('app_main:pictures')

    picture = Picture.objects.filter(pk=pic_id).first()
    return render(request, "app_main/edit.html", 
                  context={"title": "pictures output", "pic": picture, "media":settings.MEDIA_URL})
