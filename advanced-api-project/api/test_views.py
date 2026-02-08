from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Comprehensive test suite for the Book API endpoints.
    CRUD operations (Create, Read, Update, Delete)
    Filtering, searching, and ordering functionalities
    Authentication and permission enforcement
    
    """
    
    def setUp(self):
        """
        Set up test data and authentication for each test.
        """
        # Create test users
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass123'
        )
        
        # Create test authors
        self.author1 = Author.objects.create(name="John Smith")
        self.author2 = Author.objects.create(name="Jane Doe")
        
        # Create test books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author=self.author1,
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Python Programming",
            author=self.author2,
            publication_year=2019
        )
        self.book3 = Book.objects.create(
            title="Advanced Django",
            author=self.author1,
            publication_year=2021
        )
        
        # Initialize API client
        self.client = APIClient()
    
    #  CRUD OPERATION TESTS 
    
    def test_create_book_authenticated(self):
        """
        Test creating a book with an authenticated user.
        Expected: Book is created successfully with status 201.
        """
        self.client.login(username='testuser', password='testpass123')
        
        url = reverse('book-create')
        data = {
            'title': 'New Test Book',
            'author': self.author1.id,
            'publication_year': 2022
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)  
        self.assertEqual(response.data['title'], 'New Test Book')
    
    def test_create_book_unauthenticated(self):
        """
        Test creating a book without authentication.
        Expected: Request is forbidden with status 403 or 401.
        """
        url = reverse('book-create')
        data = {
            'title': 'Unauthorized Book',
            'author': self.author1.id,
            'publication_year': 2022
        }
        
        response = self.client.post(url, data, format='json')
        
        # Should be either 401 (Unauthorized) or 403 (Forbidden)
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
        )
    
    def test_retrieve_book_list(self):
        """
        Test retrieving the list of all books.
        Expected: Returns all books with status 200.
        """
        url = reverse('book-list') 
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) 
    
    def test_retrieve_single_book(self):
        """
        Test retrieving a single book by ID.
        Expected: Returns the specific book with status 200.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Django for Beginners')
        self.assertEqual(response.data['publication_year'], 2020)
    
    def test_update_book_authenticated(self):
        """
        Test updating a book with an authenticated user.
        Expected: Book is updated successfully with status 200.
        """
        self.client.login(username='testuser', password='testpass123')
        
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            'title': 'Updated Django Book',
            'author': self.author1.id,
            'publication_year': 2023
        }
        
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh from database
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Django Book')
        self.assertEqual(self.book1.publication_year, 2023)
    
    def test_update_book_unauthenticated(self):
        """
        Test updating a book without authentication.
        Expected: Request is forbidden with status 403 or 401.
        """
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            'title': 'Unauthorized Update',
            'author': self.author1.id,
            'publication_year': 2023
        }
        
        response = self.client.put(url, data, format='json')
        
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
        )
    
    def test_delete_book_authenticated(self):
        """
        Test deleting a book with an authenticated user.
        Expected: Book is deleted successfully with status 204.
        """
        self.client.login(username='testuser', password='testpass123')
        
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)  # 3 - 1 = 2
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())
    
    def test_delete_book_unauthenticated(self):
        """
        Test deleting a book without authentication.
        Expected: Request is forbidden with status 403 or 401.
        """
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        
        response = self.client.delete(url)
        
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
        )
        # Verify book still exists
        self.assertTrue(Book.objects.filter(pk=self.book1.pk).exists())
    
    # FILTERING TESTS 
    
    def test_filter_books_by_title(self):
        """
        Test filtering books by exact title.
        Expected: Returns only books matching the title filter.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'title': 'Django for Beginners'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django for Beginners')
    
    def test_filter_books_by_author(self):
        """
        Test filtering books by author ID.
        Expected: Returns only books by the specified author.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'author': self.author1.id})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # author1 has 2 books
    
    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        Expected: Returns only books from the specified year.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'publication_year': 2020})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2020)
    
    # SEARCHING TESTS 
    
    def test_search_books_by_title(self):
        """
        Test searching books by title text.
        Expected: Returns books with title containing search query.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'search': 'Django'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
    
    def test_search_books_by_author_name(self):
        """
        Test searching books by author name.
        Expected: Returns books by authors matching the search query.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'search': 'John'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return books by "John Smith"
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_search_no_results(self):
        """
        Test searching with a query that has no matches.
        
        Expected: Returns empty list with status 200.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'search': 'NonexistentBook'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
    
    # ORDERING TESTS 
    
    def test_order_books_by_title_ascending(self):
        """
        Test ordering books by title in ascending order.
        Expected: Returns books sorted alphabetically by title.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'ordering': 'title'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))
    
    def test_order_books_by_title_descending(self):
        """
        Test ordering books by title in descending order.
        Expected: Returns books sorted reverse-alphabetically by title.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'ordering': '-title'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles, reverse=True))
    
    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        Expected: Returns books sorted by publication year (oldest first).
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {'ordering': 'publication_year'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
    
    #  COMBINED FUNCTIONALITY TESTS 
    
    def test_filter_search_and_order_combined(self):
        """
        Test combining filtering, searching, and ordering.  
        Expected: Returns filtered, searched, and ordered results.
        """
        url = reverse('book-list')
        
        response = self.client.get(url, {
            'search': 'Django',
            'ordering': '-publication_year'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should have Django books ordered by year descending
        if len(response.data) > 1:
            years = [book['publication_year'] for book in response.data]
            self.assertEqual(years, sorted(years, reverse=True))
    
    #  PERMISSION TESTS 
    
    def test_list_view_accessible_without_auth(self):
        """
        Test that list view is accessible without authentication.
        Expected: Returns books with status 200 (IsAuthenticatedOrReadOnly).
        """
        url = reverse('book-list')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detail_view_accessible_without_auth(self):
        """
        Test that detail view is accessible without authentication.
        Expected: Returns book details with status 200.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)