from types import MappingProxyType

VERSIONING = 'rest_framework.versioning.AcceptHeaderVersioning'
PAGINATION = 'rest_framework.pagination.PageNumberPagination'

REST_FRAMEWORK_SETTINGS = MappingProxyType(
    mapping={
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
        ),
        'DEFAULT_PERMISSION_CLASSES': (),
        'DEFAULT_VERSIONING_CLASS': VERSIONING,
        'DEFAULT_VERSION': '1.0',
        'ALLOWED_VERSIONS': ('1.0',),
        'DEFAULT_PAGINATION_CLASS': PAGINATION,
        'PAGE_SIZE': 30,
    },
)
