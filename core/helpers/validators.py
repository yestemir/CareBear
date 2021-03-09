from types import MappingProxyType
from typing import Tuple

BASE_MODULE = 'django.contrib.auth.password_validation'

DEFAULT_VALIDATORS: Tuple = (
    MappingProxyType(mapping={
        'NAME': f'{BASE_MODULE}.UserAttributeSimilarityValidator',
    }), MappingProxyType(mapping={
        'NAME': f'{BASE_MODULE}.MinimumLengthValidator',
    }), MappingProxyType(mapping={
        'NAME': f'{BASE_MODULE}.CommonPasswordValidator',
    }), MappingProxyType(mapping={
        'NAME': f'{BASE_MODULE}.NumericPasswordValidator',
    }),
)
