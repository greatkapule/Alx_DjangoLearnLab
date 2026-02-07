from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books with advanced query capabilities.
    
    Functionality:
    - Filtering: Allows filtering by 'title', 'author', and 'publication_year'.
    - Searching: Enables text search across 'title' and 'author'.
    - Ordering: Supports sorting results by 'title' and 'publication_year'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Configure the backends for filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    # Step 1: Filtering - Exact matches
    # Note: If 'author' is a ForeignKey, use 'author__name' to avoid FieldError
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Step 2: Searching - Partial matches
    # Note: Use 'author__name' if 'author' is a related model
    search_fields = ['title', 'author']
    
    # Step 3: Ordering - Sorting results
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book instance by its ID (Primary Key).
    Accessible to everyone for reading.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book instance.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom save logic: can be used to set the author 
        automatically or perform validation before saving.
        """
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book instance.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book instance.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]