from django import forms
from blog.models import Category,Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
        }
        labels = {
            'category_name': 'Category Name',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category','short_description','blog_body', 'featured_image', 'status', 'is_featured')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'short_description': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter short description','rows':3}),
            'blog_body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter blog body','rows':6}),
            'featured_image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-select'}),
            'is_featured': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
        labels = {
            'title': 'Title',
            'category': 'Category',
            'short_description': 'Short Description',
            'blog_body': 'Content',
            'featured_image': 'Featured Image',
            'status': 'Status',
            'is_featured': 'Is Featured',
        }