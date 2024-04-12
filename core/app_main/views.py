from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "app_main/index.html", context={"title": "app_main"})

def upload(request):
    return render(request, "app_main/upload.html", context={"title": "upload image"})

def pictures(request):
    return render(request, "app_main/pictures.html", context={"title": "pictures output"})
