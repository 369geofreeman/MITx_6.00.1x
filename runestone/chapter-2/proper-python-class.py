# Writing a proper Python class



# A class that works well in the Python ecosystem.

# Each class should have a docstring to provide some level of documentation on how to use the class.
# 
# Each class should have a __str__ magic method to give it a meaninigful string representation.
# 
# Each class should have a proper __repr__ magic method for representation in the interactive shell, the debugger, and other cases where string conversion does not happen.
# 
# Each class should be comparable so it can be sorted and meaningfully compared with other instances. At a minimum this means implementing __eq__ and __lt__.
# 
# You should think about access control each instance variable. Which attributes do you want to make public, which attributes do you want to make read only, and which attributes do you want to control or do value checking on before you allow them to be changed.
# 
# If the class is a container for other classes then there are some further considerations:
# 
# You should be able to find out how many things the container holds using len
# 
# You should be able to iterate over the items in the container.
# 
# You may want to allow users to access the items in the container using the square bracket index notation.



# In this example we build a basic implementation of the MSDie class:

import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)


my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)

