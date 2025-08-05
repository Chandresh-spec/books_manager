from django.shortcuts import render,redirect,get_object_or_404
from .models import Author,Book,Review,Rating,Profile,CartItem,Comment
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm,EditProfile,CommentForm
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



def Cart_view(request):
    item=CartItem.objects.all()
    return render(request,'cart.html',{'item':item})




def profile_edit(request):
    profile,created=Profile.objects.get_or_create(user=request.user)
    if request.method=='POST':
        form=EditProfile(request.POST, request.FILES,instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile') 
        
        else:
            return render(request,'profile_edit.html',{'form':form})
    
    else:
        form=EditProfile(instance=profile)
        return render(request,'profile_edit.html',{'form':form})





def course_detail(request, pk):
    course = get_object_or_404(Book, pk=pk)
    comments = course.comments.filter(parent__isnull=True)  # Only top-level comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        parent_id = request.POST.get('parent_id')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.user = request.user
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
                comment.parent = parent_comment
            comment.save()
            return redirect('course_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'course_detail.html', {
        'course': course,
        'comments': comments,
        'form': form,
    })
