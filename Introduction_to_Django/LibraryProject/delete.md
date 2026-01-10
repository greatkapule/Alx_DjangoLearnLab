book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected output: Book deleted. QuerySet is now empty: <QuerySet []>