# Removing Elements




# Take an array and remove every second element out of that array. Always keep the first element and start removing with the next element.
# 
# Example:
# 
# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]


def remove_every_other(my_list):
    # Your code here!
    return [v for i,v in enumerate(my_list, 0) if not i%2]




print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#  [1, 3, 5, 7, 9]))
