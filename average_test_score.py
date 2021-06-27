from exceptions import OutsideRangeError
from shared_functions import in_range


def calculate_average_test_score(math, english, science):
    if in_range(math) and in_range(english) and in_range(science):
        return round(((math + english + science) / 3), 2)
    return 0
