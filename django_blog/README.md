# Django Blog Authentication System

## Overview
This project implements a complete user authentication system for a Django blog application.
It includes user registration, login, logout, and profile management.

## Features
- User registration with username, email, and password
- Secure login and logout using Django authentication
- Profile viewing and editing
- CSRF protection
- Password hashing

## How Authentication Works
1. Users register using a form extending Django's UserCreationForm.
2. Passwords are hashed automatically by Django.
3. Login and logout are handled using Django's built-in authentication views.
4. Profile updates use Django ModelForms.

## Testing Instructions
1. Run the server:
   ```bash
   python3 manage.py runserver

# Django Blog - CRUD Application

## Overview
A full-featured blog application built with Django and PostgreSQL that allows users to create, read, update, and delete blog posts.

## Features
- **Create Posts**: Authenticated users can create new blog posts
- **Read Posts**: All users can view blog posts
- **Update Posts**: Authors can edit their own posts
- **Delete Posts**: Authors can delete their own posts
- **User Authentication**: Login/logout functionality
- **Permissions**: Only post authors can edit/delete their posts

## Technology Stack
- **Backend**: Django 5.x
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (no JavaScript framework)

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### Setup Steps
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Create PostgreSQL database
6. Update database settings in `settings.py`
7. Run migrations: `python manage.py migrate`
8. Create superuser: `python manage.py createsuperuser`
9. Run server: `python manage.py runserver`

## URL Patterns
- `/` - List all posts
- `/posts/` - List all posts
- `/posts/new/` - Create new post (requires login)
- `/posts/<id>/` - View post details
- `/posts/<id>/edit/` - Edit post (requires author)
- `/posts/<id>/delete/` - Delete post (requires author)

## Permissions
- **List & Detail Views**: Public access
- **Create View**: Requires authentication
- **Update & Delete Views**: Requires authentication + author ownership

## Models

### Post
- `title`: CharField (max 200 characters)
- `content`: TextField
- `author`: ForeignKey to User
- `created_at`: DateTimeField (auto)
- `updated_at`: DateTimeField (auto)

## Testing
- Test all CRUD operations
- Verify permissions (non-authors cannot edit/delete)
- Test form validation
- Verify navigation between pages

## Author
Created for ALX Django Learning Lab

## Comment System

- Add Comment: Authenticated users can comment on any post via the detail page.

- Edit/Delete: Only the author of the comment can modify or remove it (enforced by UserPassesTestMixin).

- Relationship: Uses a ForeignKey relationship between Post and Comment.

## Advanced Features
- **Tagging:** Posts can be tagged using `django-taggit`. Use the 'tags' field in the post form.
- **Search:** Users can search for posts by title, content, or tags using the search bar.
- **Filtering:** Clicking on a tag badge filters posts by that specific tag.