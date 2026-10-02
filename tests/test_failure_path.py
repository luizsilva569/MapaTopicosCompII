import pytest


def parse_positive_number(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise ValueError("value must be positive")
    return parsed


def test_invalid_input_is_rejected() -> None:
    with pytest.raises(ValueError):
        parse_positive_number("0")
