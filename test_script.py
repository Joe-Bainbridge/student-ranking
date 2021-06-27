from average_test_score import calculate_average_test_score
from progress_score import calculate_progress_score
from random import randint


def test_progress_score():
    assert calculate_progress_score() == 0


def test_average_test_score():
    # example test case
    assert calculate_average_test_score(75, 65, 82) == 74
    # example test case with decimal
    assert calculate_average_test_score(88, 96, 54) == 79.33
    # edge cases
    assert calculate_average_test_score(0, 0, 0) == 0
    assert calculate_average_test_score(100, 100, 100) == 100
    # near edge cases
    assert calculate_average_test_score(1, 1, 1) == 1
    assert calculate_average_test_score(99, 99, 99) == 99
    # decimal and near edge cases
    assert calculate_average_test_score(1, 4, 2) == 2.33
    assert calculate_average_test_score(99, 96, 98) == 97.67
    # random values
    for x in range(100):
        val1 = randint(0, 100)
        val2 = randint(0, 100)
        val3 = randint(0, 100)
        expected_val = round((val1 + val2 + val3) / 3, 2)
        assert calculate_average_test_score(val1, val2, val3) == expected_val
