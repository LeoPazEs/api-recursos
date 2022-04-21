from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from rest_framework.serializers import ValidationError

def validatar_data_futuro(data):
    if data < timezone.localtime(timezone.now()).date():
        raise ValidationError(
            _('Date is invalid.'),
        ) 

