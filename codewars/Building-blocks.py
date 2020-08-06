# Building blocks


# Write a class Block that creates a block (Duh..)
# 
# ##Requirements
# 
# The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.
# 
# Define these methods:
# 
# `get_width()` return the width of the `Block`
# 
# `get_length()` return the length of the `Block`
# 
# `get_height()` return the height of the `Block`
# 
# `get_volume()` return the volume of the `Block`
# 
# `get_surface_area()` return the surface area of the `Block`
# ##Examples
# 
#     b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
# 
#     b.get_width() -> return 2
# 
#     b.get_length() -> return 4
# 
#     b.get_height() -> return 6
# 
#     b.get_volume() -> return 48
# 
#     b.get_surface_area() -> return 88
# Note: no error checking is needed




class Block:
    def __init__(self, arr):
        self.width = arr[0]
        self.length = arr[1]
        self.height = arr[2]

    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        return (self.width*self.length)*self.height
    def get_surface_area(self):
        return (2*(self.length*self.width))+(2*(self.length*self.height))+(2*(self.height*self.width))



block1 = Block([2,2,2])
print(block1.get_width())
#,2)
print(block1.get_length())
#,2)
print(block1.get_height())
#,2)
print(block1.get_volume())
# ,8)
print(block1.get_surface_area())
#,24)
