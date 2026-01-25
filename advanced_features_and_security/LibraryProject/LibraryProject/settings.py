from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-n@j8(9g^6+761qknk*6l4rz3x1@^f!d#0-o31qb_k9_l1c#ot@'

# Note: DEBUG = False is required in production to avoid exposing sensitive info
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bookshelf',
    'relationship_app',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
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


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

LOGIN_REDIRECT_URL = 'list_books'
LOGOUT_REDIRECT_URL = 'login'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Enables browser XSS filter to protect against some cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevents the site from being embedded in frames to avoid clickjacking attacks
X_FRAME_OPTIONS = 'DENY'

# Stops the browser from guessing content types to prevent certain attacks
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensures CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Ensures session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Content Security Policy (CSP)
# CSP prevents loading scripts, styles, or other resources from untrusted sources,
# which reduces the risk of Cross-Site Scripting (XSS) attacks.
# Only allow resources (images, scripts, styles, etc.) from the same origin
CSP_DEFAULT_SRC = ("'self'",)

# Only allow JavaScript to be loaded from the same origin
CSP_SCRIPT_SRC = ("'self'",)

# Only allow CSS/styles to be loaded from the same origin
CSP_STYLE_SRC = ("'self'",)

