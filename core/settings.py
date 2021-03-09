# TODO: always check for "python manage.py check --deploy"
import os
from os.path import dirname, abspath, join
from types import MappingProxyType
from typing import Tuple, Dict, List, Callable, Any

import sentry_sdk
from corsheaders.defaults import default_methods, default_headers
from environ import Env
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from .helpers import (
    DEFAULT_APPS, DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES,
    DEFAULT_MIDDLEWARE, REST_FRAMEWORK_SETTINGS, STORAGES,
    DEFAULT_STORAGE, DEFAULT_TEMPLATES, DEFAULT_VALIDATORS,
)

BASE_DIR: str = dirname(dirname(abspath(__file__)))
# Environment variables
env: Env = Env()
Env.read_env()
# Sentry
SENTRY_DSN: str = env.str(var='SENTRY_DSN')
sentry_sdk.init(
    dsn=SENTRY_DSN, integrations=(DjangoIntegration(), CeleryIntegration())
)
# Django
DEBUG: bool = env.bool(var='DEBUG')
SECRET_KEY: str = env.str(var='SECRET_KEY')
APPEND_SLASH: bool = True
ALLOWED_HOSTS: Tuple = ('*',)
INSTALLED_APPS: Tuple = DEFAULT_APPS
MIDDLEWARE: Tuple = DEFAULT_MIDDLEWARE
ROOT_URLCONF: str = 'core.urls'
TEMPLATES: Tuple = DEFAULT_TEMPLATES
WSGI_APPLICATION: str = 'core.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

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
TIME_ZONE: str = env.str(var='TIME_ZONE')
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
    env.str(var='WHERE_TO_KEEP_MEDIA'), DEFAULT_STORAGE
)
# Celery
CELERY_BROKER_URL: str = env.str(var='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND: str = env.str(var='CELERY_RESULT_BACKEND')
CELERY_TIMEZONE: str = env.str(var='CELERY_TIMEZONE')
CELERY_ENABLE_UTC: bool = True
CELERY_ACCEPT_CONTENT: Tuple = ('application/json',)
CELERY_TASK_SERIALIZER: str = 'json'
CELERY_RESULT_SERIALIZER: str = 'json'
CELERY_TASK_ACKS_LATE: bool = True
# Silk
SILKY_PYTHON_PROFILER: bool = True
SILKY_META: bool = True
SILKY_INTERCEPT_PERCENT: int = env.int(var='SILKY_INTERCEPT_PERCENT')
SILKY_MAX_RECORDED_REQUESTS: int = 8192
SILKY_AUTHENTICATION: bool = True
SILKY_AUTHORISATION: bool = True
SILKY_PERMISSIONS: Callable[[Any], Any] = lambda user: user.is_superuser
# Centrifugo
CENTRIFUGO_URL = env.str(var='CENTRIFUGO_URL')
CENTRIFUGO_API_KEY = env.str(var='CENTRIFUGO_API_KEY')
CENTRIFUGO_SECRET = env.str(var='CENTRIFUGO_SECRET')
CENTRIFUGO_NAMESPACE = env.str(var='CENTRIFUGO_NAMESPACE')
