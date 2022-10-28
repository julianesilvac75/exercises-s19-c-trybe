import pytest
from codigo import is_odd, divide


def test_is_odd_when_number_is_odd_returns_true():
    'Para um numero impart a funcao deve retornar o valor True.'
    assert is_odd(3) is True


def test_is_odd_when_number_is_even_returns_false():
    'Para um numero par a funcao deve retornar o valor False.'
    assert is_odd(2) is False


def test_divide_when_other_number_is_zero_raises_an_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(2, 0)