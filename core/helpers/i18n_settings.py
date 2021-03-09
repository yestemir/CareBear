from os.path import join, abspath, dirname
from typing import Tuple, List

from django.utils.translation import gettext_lazy as _

from .default_apps import PROJECT_APPS


def locale_path_for_app(app: str) -> str:
    return join(
        dirname(dirname(dirname(abspath(__file__)))), f'{app}/locale'
    )


DEFAULT_LOCALE_PATHS: List = [
    locale_path_for_app(app=app) for app in PROJECT_APPS
]
DEFAULT_LANGUAGES: Tuple = (
    ('en', _('English')), ('ru', _('Russian')), ('kz', _('Kazakh')),
)
