# Counting Array Elements


# Write a function that takes an array and counts the number of each unique element present.

# count(['james', 'james', 'john']) 
#=> { 'james' => 2, 'john' => 1}

def count(array):
    aDict = {}
    for i in array:
        if i in aDict:
            aDict[i] +=1
        else:
            aDict[i] = 1
    return aDict

# def count(array):
#     return {x: array.count(x) for x in array}


print(count(['a', 'a', 'b', 'b', 'b'] ))
# { 'a': 2, 'b': 3 })
