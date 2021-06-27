# Student ranking program


##### This program is made up of three files:

- progress_score.py
- average_test_score.py
- test_script.py

***progress_score.py*** contains the function named calculate_progress_score,
which takes the mock result and actual result from exams for a subject, and 
returns the progress score for these values.

***average_test_score.py*** contains the function named calculate_average_test_score.py,
which takes the scores for three subjects, math, english and science, and returns the 
average score across these.

***test_script.py*** contains the tests for the above functions. The tests consist of 
tests using the example data, edge case data, near edge case data, random data and more. 


---
To run tests, type the command pytest in the terminal of a virtual environment with 
pytest installed.

For development and testing, a virtual environment created using the pycharm IDE was used.

The dependency manager pipenv was used for this project.

To run the example program, run the example_program.py file

---

In this project I used test driven development. This means that I wrote the tests before I 
wrote the code. This made it easy to test my code as I was developing, and ensured my solution
gave accurate results.

---

##### Extended features
- [x] Expand testing to include tests for cases with error or outside range values.
- [ ] Add print statement to the tests so the user can see what happens as the tests are ran.
- [x] Example program to showcase functions. Program will take data from file, and use the
functions using some of this data, and then print a report with the results
- [ ] Allow example program to have other inputs than a text file, such as a .csv file or excel
document
- [ ] Make example program print report in a formatted table
