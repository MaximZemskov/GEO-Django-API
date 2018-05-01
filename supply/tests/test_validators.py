import pytest
from django.core.exceptions import ValidationError

from supply.validators import validate_phonenumber


def test_valid_phonenumber():
    assert validate_phonenumber('+79161111111') is None


def test_valid_regexp_match():
    with pytest.raises(ValidationError) as excinfo:
        validate_phonenumber('asdadsadsdsa')
        assert 'не равна' in str(excinfo.value)
