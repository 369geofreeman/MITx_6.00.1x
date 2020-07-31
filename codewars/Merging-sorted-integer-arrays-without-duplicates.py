# Merging-sorted-integer-arrays-(without duplicates)



# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.





def merge_arrays(first, second):
    return sorted(list(set(first+second)))



print(merge_arrays([1, 3, 5], [2, 4, 6]))
# [1, 2, 3, 4, 5, 6]
