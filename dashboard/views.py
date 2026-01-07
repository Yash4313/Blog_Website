from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Category, Post
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm, AddUserForm , EditUserForm
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Post.objects.all().count()
    users_count = User.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
        'user_count': users_count,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')



@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')   
    
    else:

        form = CategoryForm()
    context = {
        'form': form
    }

    return render(request, 'dashboard/add_category.html', context)



@login_required(login_url='login')
def edit_category(request, id):
    category  = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)



@login_required(login_url='login')
def delete_category(request, id):
    category  = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories')


@login_required(login_url='login')
def posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)


@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # Handle file uploads
        if form.is_valid():
            post = form.save(commit=False) # Create Post object but don't save to DB yet
            post.author = request.user  # Set the author to the current logged-in user
            post.save()
            title = form.cleaned_data['title'] # For any additional processing if needed
            post.slug = slugify(title) + '-' + str(post.id) # Ensure unique slug
            post.save() # Now save the Post object to the database
            return redirect('posts')
        else:
            print(form.errors)  # For debugging purposes
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)


@login_required(login_url='login')
def edit_post(request, id):
    post =get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id) # Ensure unique slug
            post.save()
            return redirect('posts')

    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context) 

@login_required(login_url='login')
def delete_post(request,id):
    post  = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('posts')


@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context={
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)


@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = AddUserForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)

@login_required(login_url='login')
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'dashboard/edit_user.html', context)

@login_required(login_url='login')
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users')