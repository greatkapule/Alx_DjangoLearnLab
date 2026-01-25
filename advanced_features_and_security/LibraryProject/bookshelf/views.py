from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, BookSearchForm, ExampleForm  

# VIEW: List all books
# Lists all books in the library.
# Permission: Only users with 'can_view' permission can access.
# Safe ORM: Uses Django ORM to fetch all books, preventing raw SQL usage.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Safe ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books})

# VIEW: Search books
# Allows users to search books by title.
# Permission: Only users with 'can_view' permission can search.
# Safe ORM: filter() with parameterized queries prevents SQL injection.
# CSRF protection: Ensured in template with {% csrf_token %}
@permission_required('bookshelf.can_view', raise_exception=True)
def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()  # Default empty queryset

    if form.is_valid():
        user_input = form.cleaned_data['title']
        # Safe query using ORM
        books = Book.objects.filter(title__icontains=user_input)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

# VIEW: Create a book
# Handles creating a new book.
# Permission: Only users with 'can_create' permission can create books.
# CSRF protection: Template form must include {% csrf_token %}.
# Form validation: Ensures input is safe and properly formatted.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Safe ORM insertion
            return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

# VIEW: Edit a book
# Allows editing an existing book.
# Permission: Only users with 'can_edit' permission can edit books.
# CSRF protection: Template includes {% csrf_token %}.
# Form validation: Ensures safe updates.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Safe retrieval
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Safe ORM update
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/form_example.html', {'form': form, 'book': book})

# VIEW: Delete a book
# Allows deleting an existing book.
# Permission: Only users with 'can_delete' permission can delete books.
# CSRF protection: Template includes {% csrf_token %}.
# Safe ORM: Deletion is done via Django ORM.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Safe retrieval
    if request.method == "POST":
        book.delete()  # Safe ORM deletion
        return redirect('list_books')

    # GET request renders a confirmation page
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})

# VIEW: ExampleForm
# Dummy view to ensure ExampleForm exists and can be rendered.
# Permission: Optional; accessible to any user for demonstration.
def example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
