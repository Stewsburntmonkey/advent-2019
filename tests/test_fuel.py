from advent.fuel import fuel_for_fuel, launch_fuel_required, module_fuel_required


def test_launch_fuel_required():
    tests = [
        {
            'input': 12,
            'expected': 2
        },
        {
            'input': 14,
            'expected': 2
        },
        {
            'input': 1969,
            'expected': 654
        },
        {
            'input': 100756,
            'expected': 33583
        },
    ]

    for test in tests:
        assert launch_fuel_required(test['input']) == test['expected']


def test_fuel_for_fuel():
    tests = [
        {
            'input': 2,
            'expected': 0
        },
        {
            'input': 654,
            'expected': 312
        },
    ]

    for test in tests:
        assert fuel_for_fuel(test['input']) == test['expected']


def test_total_fuel_required():
    tests = [
        {
            'input': 14,
            'expected': 2
        },
        {
            'input': 1969,
            'expected': 966
        },
        {
            'input': 100756,
            'expected': 50346
        },
    ]

    for test in tests:
        assert module_fuel_required(test['input']) == test['expected']