from django.shortcuts import render
from .forms import PictureForm
from .models import Picture

# Create your views here.
def main(request):
    return render(request, "app_main/index.html", context={"title": "app_main"})

def upload(request):
    form = PictureForm(instance=Picture()) # bind Picture-model to PictureForm
    return render(request, "app_main/upload.html", context={"title": "upload image", "form": form})

def pictures(request):
    return render(request, "app_main/pictures.html", context={"title": "pictures output"})
