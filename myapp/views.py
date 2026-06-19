from django.shortcuts import render
from .models import Cloth, Fruit

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def clothes(request):
    obj = Cloth.objects.all()
    return render(request, 'myapp/clothes.html', {'kapda': obj})


def fruits(request):
    obj  = Fruit.objects.all()
    return render(request, 'myapp/fruits.html', {'fal': obj})
