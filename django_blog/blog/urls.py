from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Registration
    path('register/', views.register, name='register'),
    
    # Login - using Django's built-in view
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # Logout - using Django's built-in view
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
]