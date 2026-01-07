from django import forms
from blog.models import Category,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff','is_active','groups','user_permissions' ,'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':' Enter email'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['groups'].widget.attrs.update({'class': 'form-select'})
        self.fields['user_permissions'].widget.attrs.update({'class': 'form-select'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff','is_active','groups','user_permissions')

    # defining init method to customize form fields
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':' Enter email'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['groups'].widget.attrs.update({'class': 'form-select'})
        self.fields['user_permissions'].widget.attrs.update({'class': 'form-select'})