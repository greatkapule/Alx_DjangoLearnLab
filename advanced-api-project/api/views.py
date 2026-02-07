from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List view for the Book model that supports advanced querying.
    Functionality:
    - Filtering: Use query parameters to filter by title, author ID, or publication_year.
      Example: /api/books/?publication_year=1949
    - Searching: Use the 'search' parameter to perform a text search across title and author name.
      Example: /api/books/?search=Orwell
    - Ordering: Use the 'ordering' parameter to sort results.
      Example: /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Integrated backends for filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # 1. Filtering: Allows exact matches on these fields
    # Note: 'author' filters by the Author's ID (ForeignKey)
    filterset_fields = ['title', 'author', 'publication_year']

    # 2. Searching: Allows partial text matches
    # We use 'author__name' to search the 'name' field in the related Author model
    search_fields = ['title', 'author__name']

    # 3. Ordering: Specifies which fields the user can sort by
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title


class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by its ID. Accessible to all users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """Creates a new book. Requires user authentication."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Logic to save a new book instance."""
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """Updates an existing book instance. Requires user authentication."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """Deletes a book instance. Requires user authentication."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]