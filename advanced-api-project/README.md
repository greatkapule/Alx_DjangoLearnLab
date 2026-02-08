# Advanced API Project – Django REST Framework

## Overview
This project demonstrates advanced API development using Django REST Framework.
It includes custom serializers, nested relationships, and generic class-based views
to efficiently handle CRUD operations.

## Book API Endpoints

| Endpoint | Method | Description | Access |
|--------|--------|-------------|--------|
| /api/books/ | GET | List all books | Public |
| /api/books/<id>/ | GET | Retrieve a single book | Public |
| /api/books/create/ | POST | Create a new book | Authenticated |
| /api/books/<id>/update/ | PUT/PATCH | Update a book | Authenticated |
| /api/books/<id>/delete/ | DELETE | Delete a book | Authenticated |

## Permissions
- Read operations are open to all users.
- Create, update, and delete operations require authentication.

## Technologies Used
- Django
- Django REST Framework
- SQLite

# Advanced API Project - Filtering, Searching, and Ordering

## API Endpoints

### Book List - `/api/books/`

This endpoint supports filtering, searching, and ordering of books.

#### Filtering

Filter books by specific field values:

- **By Title**: `?title=<book_title>`
  - Example: `/api/books/?title=Django`
  
- **By Author**: `?author=<author_name>`
  - Example: `/api/books/?author=Smith`
  
- **By Publication Year**: `?publication_year=<year>`
  - Example: `/api/books/?publication_year=2020`
  
- **Books Published After Year**: `?publication_year__gt=<year>`
  - Example: `/api/books/?publication_year__gt=2015`
  
- **Books Published Before Year**: `?publication_year__lt=<year>`
  - Example: `/api/books/?publication_year__lt=2020`

#### Searching

Search across title and author fields:

- **Search Query**: `?search=<query>`
  - Example: `/api/books/?search=Python`

#### Ordering

Sort results by specified fields:

- **Order by Title (Ascending)**: `?ordering=title`
- **Order by Title (Descending)**: `?ordering=-title`
- **Order by Publication Year (Ascending)**: `?ordering=publication_year`
- **Order by Publication Year (Descending)**: `?ordering=-publication_year`

#### Combining Parameters

You can combine multiple parameters:

Example: `/api/books/?search=Python&publication_year__gt=2015&ordering=-publication_year`

This searches for "Python", filters books after 2015, and orders by publication year (newest first).