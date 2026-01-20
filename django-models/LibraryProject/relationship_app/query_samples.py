from relationship_app.models import Author, Book, Library, Librarian


author = Author.objects.get(name="Chinua Achebe")
books = Book.objects.filter(author=author)


library = Library.objects.get(name="City Library")
books_in_library = library.books.all()


librarian = Librarian.objects.get(library=library)
