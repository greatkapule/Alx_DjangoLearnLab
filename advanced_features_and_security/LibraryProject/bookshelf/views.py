from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, BookSearchForm, ExampleForm  

# VIEW: List all books
# This view lists all books in the library.
# Permission check: Only users with 'can_view' permission can access.
# Safe ORM: Uses Django's ORM to fetch all books (prevents raw SQL usage)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # safe ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books})

# VIEW: Search books
# This view allows users to search books by title.
# Permission check: Only users with 'can_view' permission can search.
# Safe ORM: Uses filter() with parameterized queries to prevent SQL injection.
# CSRF protection is automatically enforced in the template using {% csrf_token %}
@permission_required('bookshelf.can_view', raise_exception=True)
def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()  # Default empty queryset

    if form.is_valid():
        user_input = form.cleaned_data['title']
        # Safe query: prevents SQL injection by using Django ORM
        books = Book.objects.filter(title__icontains=user_input)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


# VIEW: Create a book
# This view handles creating a new book.
# Permission check: Only users with 'can_create' permission can create books.
# CSRF protection: The template form must include {% csrf_token %} to prevent CSRF attacks.
# Form validation: Ensures user input is safe and correctly formatted.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Safe: input validated and saved via ORM
            return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

# VIEW: Edit a book
# This view allows editing an existing book.
# Permission check: Only users with 'can_edit' permission can edit books.
# CSRF protection: Handled by including {% csrf_token %} in the template.
# Form validation: Ensures changes are safe before saving.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Safe retrieval; 404 if book does not exist
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Safe ORM update
            return redirect('list_books')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/form_example.html', {'form': form, 'book': book})

# VIEW: Delete a book
# This view allows deleting an existing book.
# Permission check: Only users with 'can_delete' permission can delete books.
# CSRF protection: Template must include {% csrf_token %} to confirm deletion.
# Safe ORM: Deletion is done through Django ORM.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Safe retrieval
    if request.method == "POST":
        book.delete()  # Safe ORM deletion
        return redirect('list_books')

    # GET request renders a confirmation page
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})
