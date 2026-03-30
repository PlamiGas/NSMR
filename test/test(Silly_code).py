# test_main.py

from Silly_code import multiply_by_two


def test_positive_number():
    assert multiply_by_two(2) == 4


def test_zero():
    assert multiply_by_two(0) == 0


def test_negative_number():
    assert multiply_by_two(-3) == -6