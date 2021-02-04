from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UserMonitoringConfig(AppConfig):
    #name = 'user_monitoring'
    name = 'apps.user_monitoring'
    verbose_name = _('Users Monitoring Solutions')