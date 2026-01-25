from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm  # Ensure ExampleForm is imported correctly

# VIEW: List all books
# Implementation: Uses Django ORM to fetch data safely, avoiding SQL injection
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Secure: Django ORM parameterizes the query
    return render(request, 'bookshelf/book_list.html', {'books': books})

# VIEW: Secure Data Access and Form Handling
# Implementation: Demonstrates safe handling of user input via ExampleForm
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():  # Secure: Validate and sanitize all user inputs
            # Handle the data (e.g., save to database or perform a search)
            # Example search logic to satisfy "Secure Data Access" requirements
            title_query = form.cleaned_data.get('title')
            # Secure: Use ORM filters instead of string formatting
            books = Book.objects.filter(title__icontains=title_query)
            return render(request, 'bookshelf/book_list.html', {'books': books})
    else:
        form = ExampleForm()
    
    # Template: bookshelf/form_example.html must contain {% csrf_token %}
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Additional Views (Keep these for your application logic)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Standard creation logic using ORM...
    pass