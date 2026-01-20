from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author.
books = Book.objects.filter(author=Author.objects.get(name="Chinua Achebe"))


# List all books in a library.
books_in_library = Library.objects.get(name="City Library").books.all()


# Retrieve the librarian for a library.
librarian = Librarian.objects.get(library=Library.objects.get(name="City Library"))
