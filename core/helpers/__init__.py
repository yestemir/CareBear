from typing import Tuple

from .default_apps import DEFAULT_APPS
from .i18n_settings import DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES
from .default_middleware import DEFAULT_MIDDLEWARE
from .rest_framework_settings import REST_FRAMEWORK_SETTINGS
from .storages import STORAGES, DEFAULT_STORAGE
from .templates import DEFAULT_TEMPLATES
from .validators import DEFAULT_VALIDATORS

__all__: Tuple = (
    'DEFAULT_APPS', 'DEFAULT_LOCALE_PATHS', 'DEFAULT_LANGUAGES',
    'DEFAULT_MIDDLEWARE', 'REST_FRAMEWORK_SETTINGS', 'STORAGES',
    'DEFAULT_STORAGE', 'DEFAULT_TEMPLATES', 'DEFAULT_VALIDATORS',
)
