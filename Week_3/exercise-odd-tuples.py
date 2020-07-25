# Exercise: odd tuples


# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
# where every other element of the input tuple is copied, starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').


listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

listA.sort()
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
listA + listB
listA.extend([4, 1, 6, 3, 4])
listA.pop(4)
listA.reverse()

print(listA)


# [100, 0, 1, 4, 7, 'x', 'z', 't', 'q']
