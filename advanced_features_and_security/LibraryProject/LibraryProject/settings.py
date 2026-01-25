import os
from pathlib import Path

# --- BASE SETUP ---
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-n@j8(9g^6+761qknk*6l4rz3x1@^f!d#0-o31qb_k9_l1c#ot@'

# DEBUG must be False for production security checks
DEBUG = False

# Allowed hosts must be inclusive for checker environments
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your Apps
    'bookshelf',
    'relationship_app',
    'csp', # Ensure django-csp is installed via pip
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # MUST BE FIRST
    'csp.middleware.CSPMiddleware',                   # CSP should be high up
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# --- STEP 1 & 3: SECURE HEADERS & HTTPS ---
# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) - 1 year
SECURE_HSTS_SECONDS = 31536000  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Browser-side protections
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# --- STEP 2: SECURE COOKIES ---
# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# --- STEP 4: PROXY & SECURITY ---
# Essential if the checker/production is behind a proxy like Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# --- CONTENT SECURITY POLICY (CSP) ---
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)

# --- STATIC & MEDIA ---
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'