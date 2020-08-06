# Cat Dog Rabbit


#Test your understanding of what we have covered so far by trying the following exercise. Modify the code from Activecode 8 so that the final list only contains a single copy of each letter.


wordList = ['cat','dog','rabbit']
l = []
for i in wordList:
    [l.append(x) for x in i if x not in l]
print(l)




# Test your understanding of list comprehensions by redoing Activecode 8 using list comprehensions. For an extra challenge, see if you can figure out how to remove the duplicates.


print(set([i for i in "".join(wordList) ]))
