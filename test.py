# import math
# import numpy as np
# import os
import string

# print(int(((2+4*6) % 4)*1+6//7+912*3*22*math.sqrt(4) +
#           int(np.array([3])+os.system("echo 2 > /dev/null"))))


student_marks = {
    'Krishna': [67, 68, 69],
    'Arjun': [70, 98, 63],
    'Malika': [52, 56, 60],
}
query_name = 'Malika'


for i in student_marks.keys():
    if i == query_name:
        print("{:.2f}".format(sum(student_marks[i])/len(student_marks[i])))
