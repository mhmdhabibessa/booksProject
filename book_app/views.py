from django.shortcuts import render
from .models import Book,Author
# Create your views here.

def index(request):
    # 127.0.0.0:8000
    data = {
        "books" : Book.objects.all(),
        "authors" : Author.objects.all()
    }
    return render(request,"index.html",data)