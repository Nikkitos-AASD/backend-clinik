import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# ========= BASE =========

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-#0@xqjf94+wjec(=8cv!q_6izw5l+b-7+9ytu#8oxl9mj3c_i4",
)

DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# Без схемы
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "your-backend.onrender.com",  # TODO: поменяй на реальный backend URL
]

# ========= APPS =========

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "main",
    "rest_framework",
    "corsheaders",
    "csp",
]

# ========= MIDDLEWARE =========

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise (подключим после установки пакета)
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# ========= DATABASE =========
# Пока SQLite. Позже заменим на DATABASE_URL (Postgres на Render).

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {"timeout": 20},
    }
}

# ========= PASSWORDS =========

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

AUTHENTICATION_BACKENDS = [
    "main.backends.PhoneOrEmailBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "main.User"

# ========= I18N / TZ =========

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Asia/Novosibirsk"
USE_I18N = True
USE_TZ = True

# ========= STATIC / MEDIA =========

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ========= REST / JWT =========

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ========= CORS / CSRF =========

FRONTEND_URL = "https://clinik-1i8i.onrender.com"
BACKEND_URL = "https://your-backend.onrender.com"  # TODO: поменяй на реальный backend URL

CORS_ALLOWED_ORIGINS = [
    FRONTEND_URL,
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    FRONTEND_URL,
    BACKEND_URL,
]

# ========= CSP =========

CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ["'self'"],
        "script-src": ["'self'"],
        "style-src": ["'self'", "'unsafe-inline'"],
        "img-src": [
            "'self'",
            "data:",
            BACKEND_URL,
            "http://127.0.0.1:8000",
            "http://localhost:8000",
        ],
        "font-src": ["'self'", "data:"],
        "connect-src": [
            "'self'",
            BACKEND_URL,
            FRONTEND_URL,
            "http://127.0.0.1:8000",
            "http://localhost:8000",
            "http://127.0.0.1:5173",
            "http://localhost:5173",
        ],
        "frame-ancestors": ["'self'"],
        "object-src": ["'none'"],
        "base-uri": ["'self'"],
    }
}

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# ========= MISC =========

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"