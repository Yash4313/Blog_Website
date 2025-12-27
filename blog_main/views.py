from django.shortcuts import render
from blog.models import Category,Post

def home(request):
    featured_posts = Post.objects.filter(is_featured=True,status='published').order_by('-created_at')[:3]
    context = {
        'featured_posts':featured_posts,
    }
    return render(request,"home.html",context)