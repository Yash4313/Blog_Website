from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.

from blog.models import Category,Post,Comment
from django.db.models import Q

# render individual category list
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


# render individual blog post
def blogs(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    
    if request.method == 'POST':
        # Handle comment submission
        comment = Comment()
        comment.user = request.user
        comment.post = post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    category = post.category
    comments = post.comment_set.all().order_by('-created_at') #fetch comments related to the post

    context = {
        'post': post,
        'category': category,
        'comments': comments,
        'comment_count': comments.count(),
    }
    return render(request, 'blogs.html', context)

# search blog posts
def search(request):
    query = request.GET.get('keyword')
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(blog_body__icontains=query), status='published').order_by('-created_at')
    else:
        results = []
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search.html', context)