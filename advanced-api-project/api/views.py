from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Handles GET requests to retrieve a list of books.
    Supports advanced query features:
    - Filtering: ?title=...&author__name=...&publication_year=...
    - Searching: ?search=... (searches title and author name)
    - Ordering: ?ordering=title or ?ordering=publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Required backends for filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    # Use 'author__name' (or similar) if author is a ForeignKey to fix the FieldError
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Search inside the title and the related author's name
    search_fields = ['title', 'author__name']
    
    # Allow sorting by title and publication year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default sort order

class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by its ID (PK). Publicly accessible."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """Creates a new book. Requires user to be logged in."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Hook to perform actions before saving to the database
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """Updates an existing book. Requires user to be logged in."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """Deletes a book. Requires user to be logged in."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]