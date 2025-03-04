
import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    name = "accounts"
    verbose_name = _("Accounts")

    def ready(self):
        with contextlib.suppress(ImportError):
            import cash_send.accounts.signal
