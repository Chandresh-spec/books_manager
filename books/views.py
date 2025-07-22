from django.shortcuts import render
from .models import Author,Book,Review,Rating

# Create your views here.

def helo(request):
    return render(request,'index.html')


def Home_page(request):
    item=Book.objects.all()
    review=Review.objects.all()
    rating=Rating.objects.all()
    author=Author.objects.all()

    return render(request,'home.html',{'item':item,'review':review,'rating':rating,'author':author})






