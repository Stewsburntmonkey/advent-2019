from dataclasses import dataclass
from typing import Any

from advent.password import has_digit_pair, has_repeated_digits, is_valid, monotonicly_increasing


@dataclass
class TestCase:
    input: Any
    expected: Any


def test_is_valid():
    tests = [
        {
            'input': 111111,
            'expected': True,
        },
        {
            'input': 223450,
            'expected': False,
        },
        {
            'input': 123789,
            'expected': False,
        },
    ]

    for test in tests:
        assert is_valid(test['input']) == test['expected']


def test_has_repeated_digits():
    tests = [
        TestCase(110123, True),
        TestCase(123455, True),
        TestCase(123456, False),
    ]

    for test in tests:
        assert has_repeated_digits(test.input) == test.expected


def test_monotonicly_increasing():
    tests = [
        TestCase(123456, True),
        TestCase(112233, True),
        TestCase(213456, False),
        TestCase(123465, False),
    ]

    for test in tests:
        assert monotonicly_increasing(test.input) == test.expected


def test_has_digit_pair():
    tests = [
        TestCase(112233, True),
        TestCase(123444, False),
        TestCase(111122, True),
    ]

    for test in tests:
        assert has_digit_pair(test.input) == test.expected