from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    # Category Management
    path('categories/', views.categories , name='categories'),
    path('add_category/', views.add_category , name='add_category'),
    path('edit_category/<int:id>/', views.edit_category , name='edit_category'),
    path('delete_category/<int:id>/', views.delete_category , name='delete_category'),
    
    # post Management
    path('posts/', views.posts , name='posts'),
    path('posts/add/', views.add_post , name='add_post'),
    path('posts/edit/<int:id>/', views.edit_post , name='edit_post'),
    path('post/delete/<int:id>/',views.delete_post, name='delete_post'),

    # user Management
    path('users/', views.users , name='users'),
    path('users/add/', views.add_user , name='add_user'),
    path('users/edit/<int:id>/', views.edit_user , name='edit_user'),
    path('users/delete/<int:id>/',views.delete_user, name='delete_user'),
]
