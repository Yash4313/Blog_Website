from django.contrib import admin
from .models import Category,Post
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} #for auto generate slug from title
    list_display = ('title', 'status', 'author','category','is_featured') #fields to display in admin list view
    search_fields = ('id','title','author__username','category__category_name','status') #fields to search in admin
    list_editable = ('is_featured',) #fields editable in list view

admin.site.register(Category)
admin.site.register(Post,BlogAdmin)