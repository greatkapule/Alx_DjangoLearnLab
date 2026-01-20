from relationship_app.models import Author, Book, Library, Librarian


books_by_author = Book.objects.filter(author__name="Chinua Achebe")


library = Library.objects.get(name="City Library")
library_books = library.books.all()

library_librarian = Librarian.objects.get(library=library)
