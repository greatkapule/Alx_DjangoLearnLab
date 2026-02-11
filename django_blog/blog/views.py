from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm


def register(request):
    """
    Handle user registration.
    
    How it works:
    1. User visits the page (GET request) - Show empty form
    2. User submits the form (POST request) - Process the data
    3. If valid, create account and redirect to login
    4. If invalid, show errors
    """
    if request.method == 'POST':
        # User submitted the form
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            # Form data is valid, create the user
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Show success message
            messages.success(request, f'Account created for {username}! You can now log in.')
            
            # Redirect to login page
            return redirect('login')
    else:
        # User is visiting the page (GET request)
        form = CustomUserCreationForm()
    
    # Render the template with the form
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    """
    Display and handle user profile updates.
    
    @login_required decorator ensures only logged-in users can access this view.
    
    How it works:
    1. User visits profile (GET) - Show current information
    2. User updates profile (POST) - Save changes
    """
    if request.method == 'POST':
        # User is updating their profile
        form = UserUpdateForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        # Show current profile information
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})

