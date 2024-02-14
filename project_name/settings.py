"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

from environs import Env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(path=BASE_DIR.joinpath('.env'), recurse=False, override=True)

# Django debug toolbar.
INTERNAL_IPS = ['127.0.0.1', 'localhost']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': env.dj_db_url(
        'DATABASE_URL',
        default=f'sqlite:///{BASE_DIR.joinpath("dev.sqlite3")}',
        # ssl_require=not DEBUG,
    )
}

EMAIL = env.dj_email_url(
    'EMAIL_URL',
    default=f'file:///{BASE_DIR.joinpath("EMAILS")}',
)
# EMAIL_HOST = EMAIL['EMAIL_HOST']
# EMAIL_PORT = EMAIL['EMAIL_PORT']
# EMAIL_HOST_PASSWORD = EMAIL['EMAIL_HOST_PASSWORD']
# EMAIL_HOST_USER = EMAIL['EMAIL_HOST_USER']
# EMAIL_USE_TLS = EMAIL['EMAIL_USE_TLS']

CACHES = {
    'default': env.dj_cache_url(
        'CACHE_URL',
        default='dummy://',
    ),
}

# Application definition
INSTALLED_APPS = [
    # Apps.
    'accounts.apps.AccountsConfig',
    'home.apps.HomeConfig',
    # Django.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Sitemap.
    'django.contrib.sitemaps',
    # External.
    'django_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Whitenoise.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 100,
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle',
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '1/day',
#         'user': '2/day',
#     },
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom context_processors.
                # '_context_processors.example.example',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATICFILES_DIRS = (
    BASE_DIR.joinpath('static'),
)

STATIC_URL = '/public/staticfiles/'
STATIC_ROOT = BASE_DIR.joinpath('public', 'staticfiles')

MEDIA_URL = '/public/media/'
MEDIA_ROOT = BASE_DIR.joinpath('public', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Whitenoise.
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')