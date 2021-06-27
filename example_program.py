from progress_score import calculate_progress_score
from average_test_score import calculate_average_test_score


def get_progress_score(mock, actual):
    return calculate_progress_score(int(line[mock]), int(line[actual]))


def get_average_progress_score():
    return round(((progress_scores["maths"] + progress_scores["english"] + progress_scores["science"]) / 3), 2)


data_file = open('data.txt', "r")
data = []

for line in data_file:
    line_data = line.split(",")
    data.append(line_data)

progress_scores = {}

for line in data:
    progress_scores["maths"] = get_progress_score(1, 2)
    progress_scores["english"] = get_progress_score(4, 5)
    progress_scores["science"] = get_progress_score(7, 8)

    print("Student: %s" % line[0])
    print("Maths mock: %s" % line[1])
    print("Maths actual result: %s" % line[2])
    print("Maths progress score: %s" % progress_scores["maths"])
    print("\nEnglish mock: %s" % line[4])
    print("English actual result: %s" % line[5])
    print("English progress score: %s" % progress_scores["english"])
    print("\nScience mock: %s" % line[7])
    print("Science actual result: %s" % line[8])
    print("Science progress score: %s" % progress_scores["science"])
    print("\nAverage test results: %s" % calculate_average_test_score(int(line[2]), int(line[5]), int(line[8])))
    print("Average progress score: %s" % get_average_progress_score())
    print("\n------------------------------------------------------------------------\n")
