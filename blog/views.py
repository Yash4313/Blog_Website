from django.shortcuts import render

# Create your views here.

from blog.models import Category,Post

def category_list(request, category_id):
    # Fetch the category based on the provided ID
    try:
        category = Category.objects.get(id=category_id)
    except:
        return render(request, '404.html', status=404)
    # Fetch all published posts under this category
    posts = Post.objects.filter(category=category, status='published').order_by('-created_at')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'category_list.html', context)
