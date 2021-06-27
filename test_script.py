from average_test_score import calculate_average_test_score
from progress_score import calculate_progress_score
from random import randint


def test_progress_score():
    # example test cases
    assert calculate_progress_score(80, 75) == -0.5
    assert calculate_progress_score(57, 65) == -0.8
    assert calculate_progress_score(50, 80) == 3
    assert calculate_progress_score(99, 88) == -1.1
    # edge cases
    assert calculate_progress_score(100, 100) == 0
    assert calculate_progress_score(0, 0) == 0
    # near edge cases
    assert calculate_progress_score(99, 99) == 0
    assert calculate_progress_score(1, 1) == 0
    # near edge cases different values - negative
    assert calculate_progress_score(99, 96) == -0.3
    assert calculate_progress_score(3, 1) == -0.2
    # near edge cases different values - positive
    assert calculate_progress_score(96, 99) == 0.3
    assert calculate_progress_score(1, 3) == 0.2
    # random values
    for x in range(100):
        val1 = randint(0, 100)
        val2 = randint(0, 100)
        expected_val = round(((val2-val1)/10), 1)
        assert calculate_progress_score(val1, val2) == expected_val


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
