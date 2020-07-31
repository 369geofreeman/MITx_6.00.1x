#Enumerable Magic #30 - Split that Array!

# Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.
# 
# Here's a simple Ruby example:
# 
# animals = ["cat", "dog", "duck", "cow", "donkey"]
# partition(animals){|animal| animal.size == 3}
#     #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
# The equivalent in Python would be:
# 
# animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
# partition(animals, lambda x: len(x) == 3)
#     # (['cat', 'dog', 'cow'], ['duck', 'donkey'])




def partition(arr, classifier_method):
    lst1 = [i for i in arr if classifier_method(i)]
    lst2 = [x for x in arr if x not in lst1]
    return lst1, lst2





animals = ["cat", "dog", "duck", "cow", "donkey"]

print(partition(animals, lambda x: len(x) == 3))
