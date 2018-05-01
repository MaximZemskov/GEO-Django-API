import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phonenumber(value):
    prog = re.compile('^((8|\+7)\d{10}$)')
    result = prog.match(value)
    if not result:
        raise ValidationError(
            _('%(value)s не верный формат номера. Используйте +79261234567'),
            params={'value': value}
        )
