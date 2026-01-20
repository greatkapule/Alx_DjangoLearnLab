from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author():
    # Query all books by a specific author.
    author = Author.objects.get(name="Chinua Achebe")
    books = Book.objects.filter(author=author)
    return books


def list_books_in_library():
    # List all books in a library.
    library = Library.objects.get(name="City Library")
    books_in_library = library.books.all()
    return books_in_library


def get_librarian_for_library():
    # Retrieve the librarian for a library.
    library = Library.objects.get(name="City Library")
    librarian = Librarian.objects.get(library=library)
    return librarian
