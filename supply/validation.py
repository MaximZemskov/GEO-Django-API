import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phonenumber(number):
    prog = re.compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    result = prog.match(number)
    if not result:
        raise ValidationError(
            _('%(number)s is not valid phone number. Use following types of number +79261234567' +
              ' 89261234567' +
              ' 79261234567' +
              ' +7 926 123 45 67' +
              ' 8(926)123-45-67' +
              ' 123-45-67' +
              ' 9261234567' +
              ' 79261234567' +
              ' (495)1234567' +
              ' (495) 123 45 67' +
              ' 89261234567' +
              ' 8-926-123-45-67' +
              ' 8 927 1234 234' +
              ' 8 927 12 12 888' +
              ' 8 927 12 555 12' +
              ' 8 927 123 8 123'),
            params={'number': number}
        )
