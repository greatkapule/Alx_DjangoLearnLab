from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    #List all books with filtering, searching, and ordering.
    #Permissions: Can be read by anyone, write restricted to authenticated users.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    #Retrieve a single book by ID.
    #Permissions: Can be read by anyone, write restricted to authenticated users.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    #Creates a new book.
    #Permissions: Authenticated users only.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    #Updates an existing book.
    #Permissions: Authenticated users only.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    #Deletes a book.
    #Permissions: Authenticated users only.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
