# Finding the percentage

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

student_marks = {
    'Krishna': [67, 68, 69],
    'Arjun': [70, 98, 63],
    'Malika': [52, 56, 60],
}
query_name = 'Malika'


for i in student_marks.keys():
    if i == query_name:
        print("{:.2f}".format(sum(student_marks[i])/len(student_marks[i])))
