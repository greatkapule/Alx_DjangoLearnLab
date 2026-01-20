import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian



author = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author)
book2 = Book.objects.create(title="No Longer at Ease", author=author)

library = Library.objects.create(name="City Library")
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="John", library=library)


books_by_author = Book.objects.filter(author__name="Chinua Achebe")
print("Books by Chinua Achebe:")
for book in books_by_author:
    print(book.title)


library_books = library.books.all()
print("\nBooks in City Library:")
for book in library_books:
    print(book.title)


library_librarian = Librarian.objects.get(library=library)
print("\nLibrarian managing City Library:")
print(library_librarian.name)
