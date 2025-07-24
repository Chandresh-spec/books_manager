from django.shortcuts import render,redirect
from .models import Author,Book,Review,Rating,Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .froms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def helo(request):
    return render(request,'index.html')


def Home_page(request):
    item=Book.objects.all()
    review=Review.objects.all()
    rating=Rating.objects.all()
    author=Author.objects.all()

    return render(request,'home.html',{'item':item,'review':review,'rating':rating,'author':author})



def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return  redirect('home_page')

        else:
            return render(request,'register.html',{'form':form})
    else:
        form=RegisterForm()
        return render(request,'register.html',{'form':form})




def logout_view(request):
    logout(request)
    return redirect('home_page')


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(username=username,password=password)

            if  user:
                login(request,user)
                return redirect('home_page')
            
           
           
        
        else:
            return render(request,'login.html',{'form':form})
    
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})




    