from django.shortcuts import render

# Create your views here.


def home_page(request):
    context = {"name": "test"}
    return render(request, "index.html")
