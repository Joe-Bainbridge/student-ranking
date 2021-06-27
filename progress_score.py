from shared_functions import in_range


def calculate_progress_score(mock_result, actual_result):
    if in_range(mock_result) and in_range(actual_result):
        return round(((actual_result - mock_result) / 10), 1)
    return 0
