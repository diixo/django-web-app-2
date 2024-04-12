from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "app_main/index.html", context={"title": "app_main"})
