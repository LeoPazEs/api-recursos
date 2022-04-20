from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

def validatar_data_devolucao(data):
    if data < datetime.now().date():
        raise ValidationError(
            _('Date is invalid.'),
        )