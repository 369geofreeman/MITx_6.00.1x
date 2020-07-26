# Exercise: apply to each

# testList = [1, -4, 8, -9]
# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that
# testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has
# the indicated value. You may need to write a simple procedure in each question to help with this process.


testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L


def testAbs(x):
    # result [1, 4, 8, 9]
    return abs(x)


def addOne(x):
    # result [2, -3, 9, -8]
    return x+1


def square(x):
    # result [1, 16, 64, 81]
    return x*x


# print(applyToEach(testList, testAbs))
# print(applyToEach(testList, addOne))
print(applyToEach(testList, square))
