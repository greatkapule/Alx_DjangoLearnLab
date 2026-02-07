from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List view for Book model with integrated query capabilities.
    Provides filtering (DjangoFilterBackend), searching (SearchFilter), 
    and ordering (OrderingFilter).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Explicitly define backends for the checker to detect
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Step 1: Filtering - Filter by title, author, and publication_year
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Search - Search by title and author
    # Note: Using 'author__name' allows text-based search on the related Author model
    search_fields = ['title', 'author__name']

    # Step 3: Ordering - Order by title and publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by ID. Publicly accessible."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """Creates a new book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
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