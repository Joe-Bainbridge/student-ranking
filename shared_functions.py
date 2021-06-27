from exceptions import OutsideRangeError


def in_range(number):
    if 0 <= number <= 100:
        return True
    else:
        raise OutsideRangeError("Value passes to function outside of range")
