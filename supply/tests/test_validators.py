import pytest
from django.core.exceptions import ValidationError

from supply.validators import validate_phonenumber, validate_service_price


def test_valid_phonenumber():
    assert validate_phonenumber('+79161111111') is None


def test_valid_phonenumber_regexp_match():
    with pytest.raises(ValidationError) as excinfo:
        validate_phonenumber('asdadsadsdsa')
        assert 'не равна' in str(excinfo.value)


def test_valid_service_price():
    assert validate_service_price('123123123') is None


def test_valid_servoce_rpice_regexp_match():
    with pytest.raises(ValidationError) as excinfo:
        validate_service_price('asdadsadsdsa')
        assert 'не равна' in str(excinfo.value)
