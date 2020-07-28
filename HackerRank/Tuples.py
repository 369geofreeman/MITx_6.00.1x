# Tuples

# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).


integer_list=[int(x) for x in integer_list]
tup = tuple(integer_list)
print(hash(tup))
