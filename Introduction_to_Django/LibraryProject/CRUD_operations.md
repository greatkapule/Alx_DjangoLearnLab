## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Retrieve
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

## Update
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

## Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

