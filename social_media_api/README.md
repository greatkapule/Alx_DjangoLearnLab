# Social Media API

A RESTful Social Media API built with Django and Django REST Framework.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Alx_DjangoLearnLab/social_media_api
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/accounts/register/` | Register a new user | No |
| POST | `/api/accounts/login/` | Login and get token | No |
| GET | `/api/accounts/profile/` | View your profile | Yes |
| PUT | `/api/accounts/profile/` | Update your profile | Yes |

---

## How to Register a User

**POST** `/api/accounts/register/`

**Request body:**
```json
{
  "username": "john_njagi",
  "email": "john@example.com",
  "password": "securepassword",
  "bio": "Hello, I'm John!"
}
```

**Response:**
```json
{
  "message": "User registered successfully.",
  "token": "your-auth-token-here",
  "user": {
    "id": 1,
    "username": "john_njagi",
    "email": "john@example.com"
  }
}
```

---

## How to Authenticate

Add this header to all protected requests:
```
Authorization: Token your-auth-token-here
```

---

## User Model Overview

The `CustomUser` model extends Django's `AbstractUser` with:

- `bio` — A short biography (text field)
- `profile_picture` — An uploaded profile image
- `followers` — ManyToMany self-referential field (asymmetric follows)