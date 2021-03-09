# TODO: always check for "python manage.py check --deploy"
import os
from os.path import dirname, abspath, join
from types import MappingProxyType
from typing import Tuple, List, Callable, Any

from corsheaders.defaults import default_methods, default_headers
from environ import Env

from .helpers import (
    DEFAULT_APPS, DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES,
    DEFAULT_MIDDLEWARE, REST_FRAMEWORK_SETTINGS, STORAGES,
    DEFAULT_STORAGE, DEFAULT_TEMPLATES, DEFAULT_VALIDATORS,
)

BASE_DIR: str = dirname(dirname(abspath(__file__)))
# Environment variables
env: Env = Env()
Env.read_env()
# Django
DEBUG: bool = True
SECRET_KEY: str = 'B81543719AB276D3268D4A293FC2A492E2B4996CCE2D6624B529351A26'
APPEND_SLASH: bool = True
ALLOWED_HOSTS: Tuple = ('*',)
INSTALLED_APPS: Tuple = DEFAULT_APPS
MIDDLEWARE: Tuple = DEFAULT_MIDDLEWARE
ROOT_URLCONF: str = 'core.urls'
TEMPLATES: Tuple = DEFAULT_TEMPLATES
WSGI_APPLICATION: str = 'core.wsgi.application'
DATABASES: MappingProxyType = MappingProxyType({'default': env.db()})
AUTH_PASSWORD_VALIDATORS: Tuple = DEFAULT_VALIDATORS
# ASGI
ASGI_APPLICATION: str = 'core.asgi.application'
# Security
SECURE_BROWSER_XSS_FILTER: bool = True
SESSION_COOKIE_SECURE: bool = False
X_FRAME_OPTIONS: str = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF: bool = True
CSRF_COOKIE_SECURE: bool = False
# Localization
LOCALE_PATHS: List = DEFAULT_LOCALE_PATHS
LANGUAGES: Tuple = DEFAULT_LANGUAGES
LANGUAGE_CODE: str = 'en'
USE_I18N: bool = True
USE_L10N: bool = True
TIME_ZONE: str = 'Asia/Almaty'
USE_TZ: bool = True
STATIC_URL: str = '/static/'
STATIC_ROOT: str = join(BASE_DIR, 'staticfiles')
MEDIA_URL: str = '/media/'
MEDIA_ROOT: str = join(BASE_DIR, 'media')
# CorsHeaders
CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ALLOW_METHODS: Tuple = default_methods
CORS_ALLOW_HEADERS: Tuple = default_headers
CORS_ALLOW_CREDENTIALS: bool = True
# Rest framework
REST_FRAMEWORK: MappingProxyType = REST_FRAMEWORK_SETTINGS
# Storage
DEFAULT_FILE_STORAGE: str = STORAGES.get(
    'LOCAL', DEFAULT_STORAGE
)
