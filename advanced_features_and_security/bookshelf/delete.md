from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected Output: Book deleted. QuerySet is now empty: <QuerySet []>