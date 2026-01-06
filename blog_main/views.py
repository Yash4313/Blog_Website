from django.shortcuts import render,redirect
from blog.models import Post
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

def home(request):
    featured_posts = Post.objects.filter(is_featured=True,status='published').order_by('-created_at')[:6]
    context = {
        'featured_posts':featured_posts,
    }
    return render(request,"home.html",context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': RegistrationForm(),
                'success': 'Registration successful! You can now log in.'
            }
            return render(request, "register.html", context)
    else:

        form = RegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, "register.html",context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")