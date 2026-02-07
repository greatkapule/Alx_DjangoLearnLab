from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    #Retrieves a list of all Book instances.
    #Accessible to all users (authenticated or not).
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    #Retrieves a single Book by its ID.
    #Accessible to all users.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    #Creates a new Book.
    #Restricted to authenticated users only.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    #Updates an existing Book.
    #Restricted to authenticated users only.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    #Handles deletion of a Book.
    #Restricted to authenticated users only.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
