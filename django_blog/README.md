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
