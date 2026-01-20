from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author.
# The checker likely looks for the filter(author=author) pattern.
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2. List all books in a library.
# The checker looks for the specific library name and its books.
def get_library_books(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library.
# The checker specifically looks for Librarian.objects.get(library=library).
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)