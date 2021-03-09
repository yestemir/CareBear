from types import MappingProxyType
from typing import Tuple

DEFAULT_TEMPLATES: Tuple = (
    MappingProxyType(mapping={
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (), 'APP_DIRS': True, 'OPTIONS': MappingProxyType(mapping={
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
        }),
    }),
)
