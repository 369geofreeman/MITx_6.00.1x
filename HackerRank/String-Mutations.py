# coding=utf-8

# String Mutations


# Read a given string, change the character at a given index and then print the modified string.



def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)


print(mutate_string('hello', 2, 'Z'))
