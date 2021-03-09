from typing import Tuple

DJANGO_MIDDLEWARE: Tuple = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
SIDE_MIDDLEWARE: Tuple = (
    'corsheaders.middleware.CorsMiddleware',
)
BEFORE: Tuple = DJANGO_MIDDLEWARE[:3]
AFTER: Tuple = DJANGO_MIDDLEWARE[3:]
DEFAULT_MIDDLEWARE: Tuple = BEFORE + SIDE_MIDDLEWARE + AFTER
