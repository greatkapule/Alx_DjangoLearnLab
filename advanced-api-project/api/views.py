from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Handles GET requests to retrieve a list of books with the following features:
    - Filtering: Users can filter by 'title', 'author__name', and 'publication_year'.
    - Searching: Users can search by 'title' and 'author__name'.
    - Ordering: Users can sort by 'title' and 'publication_year'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Explicitly define backends to ensure they are picked up by API and checkers
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    # Using 'author__name' solves the FieldError for ForeignKey fields
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Enables text-based search functionality
    search_fields = ['title', 'author__name']
    
    # Enables results to be sorted
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default sort order

class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by its ID (PK). Publicly accessible."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """Creates a new book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Custom logic applied during the creation of a book instance."""
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """Updates an existing book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """Deletes a book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]