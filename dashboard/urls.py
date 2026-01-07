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
    
]
