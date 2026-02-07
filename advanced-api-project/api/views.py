from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with advanced query capabilities.
    
    Features:
    - Filtering: ?title=value, ?author=id, ?publication_year=value
    - Searching: ?search=text (searches title and author name)
    - Ordering: ?ordering=field (e.g., ?ordering=-publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Backend integration for filtering, search, and ordering
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]

    # Step 1: Filtering - specific fields for exact matches
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Searching - text-based search across related fields
    # Use 'author__name' to perform text search on the Author model
    search_fields = ['title', 'author__name']

    # Step 3: Ordering - allows sorting by specified fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default order


class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by ID. Public access allowed."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """Creates a new book instance. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Custom save logic for book creation."""
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """Updates an existing book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """Deletes a book instance. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]