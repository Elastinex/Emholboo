from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BaseConfig(AppConfig):
    name = 'src.base'
    verbose_name = _('Base')
