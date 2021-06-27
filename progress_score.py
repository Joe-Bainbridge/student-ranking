def calculate_progress_score(mock_result, actual_result):
    return round(((actual_result-mock_result)/10), 1)
