from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    # This view integrates filtering, searching, and ordering functionalities to enhancethe usability of the API for consuming applications. 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #enable filtering, searching and ordering.
    filter_backends = [
        DjangoFilterBackend,  
        filters.SearchFilter,  
        filters.OrderingFilter  
    ]
    
    # Users can filter by these fields using query parameters.
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Allows searching by these fields.
    search_fields = ['title', 'author__name']
    
    # Users can sort results by these fields in ascending or descending order
    ordering_fields = ['title', 'publication_year']
    
    # Default ordering - Specifies default sort order when no ordering parameter is provided
    ordering = ['title']  # Default: alphabetically by title


class BookDetailView(generics.RetrieveAPIView):
    
   # Retrieves a single book instance by its primary key (ID).
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
   # Creates a new book instance.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
   # Updates an existing book instance.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):

    #Deletes a book instance.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]