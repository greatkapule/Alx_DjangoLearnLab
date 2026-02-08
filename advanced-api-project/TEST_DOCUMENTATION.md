# API Testing Documentation

## Overview
This document describes the testing strategy for the Book API endpoints in the Advanced API Project.

## Test Coverage

### CRUD Operations
- **Create**: Tests book creation with authenticated and unauthenticated users
- **Read**: Tests retrieving book lists and individual book details
- **Update**: Tests updating books with proper authentication
- **Delete**: Tests deleting books with permission checks

### Query Capabilities
- **Filtering**: Tests filtering by title, author, and publication year
- **Searching**: Tests text search across title and author fields
- **Ordering**: Tests sorting by title and publication year (ascending/descending)

### Security
- **Authentication**: Verifies that protected endpoints require authentication
- **Permissions**: Tests IsAuthenticatedOrReadOnly permission enforcement

## Running Tests

### Run All Tests
```bash
python manage.py test api
```

### Run with Detailed Output
```bash
python manage.py test api --verbosity=2
```

### Run Specific Test Class
```bash
python manage.py test api.test_views.BookAPITestCase
```

### Run Specific Test Method
```bash
python manage.py test api.test_views.BookAPITestCase.test_create_book_authenticated
```

## Test Database
Tests use Django's built-in test database which is:
- Created automatically before tests run
- Destroyed automatically after tests complete
- Completely separate from development/production databases

## Expected Results
All tests should pass with output similar to:
```
Ran 20 tests in 2.345s
OK
```

## Troubleshooting

### Authentication Failures
If tests fail with 403/401 errors:
1. Check that `permission_classes` are correctly set in views
2. Verify `self.client.login()` is called before authenticated requests
3. Ensure test users are created in `setUp()` method

### URL Resolution Errors
If tests fail with `NoReverseMatch`:
1. Verify URL names in `urls.py` match `reverse()` calls in tests
2. Check that URL patterns include all required parameters

### Database Errors
If tests fail with database errors:
1. Run migrations: `python manage.py migrate`
2. Check model relationships (ForeignKey, etc.)
3. Verify test data creation in `setUp()` method

## Test Maintenance
- Update tests when adding new endpoints
- Add tests for new filtering/search capabilities
- Test edge cases and error conditions
- Keep test data realistic but minimal