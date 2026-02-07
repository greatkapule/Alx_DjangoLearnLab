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
