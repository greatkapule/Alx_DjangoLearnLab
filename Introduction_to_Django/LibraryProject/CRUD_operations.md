# CRUD Operations Documentation

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: Book instance created successfully

## Retrieve
book = Book.objects.get(title="1984")
# Output: Title: 1984, Author: George Orwell, Year: 1949

##Update
book.title = "Nineteen Eighty-Four"
book.save()
# Output: Title updated to Nineteen Eighty-Four

## Delete
book.delete()
# Output: Book deleted. QuerySet is now empty: <QuerySet []>