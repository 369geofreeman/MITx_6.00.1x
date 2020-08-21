# Hash Table Poem word Count


# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8


words = {}

with open('poem.txt', 'r') as f:
    for line in f:
        data = line.split(' ')
        for word in data:
            word=word.replace('\n','')
            if word in words.keys():
                words[word] +=1
            else:
                words[word] = 1

for i in words.keys():
    print("'{}': {}".format(i,words[i]))
