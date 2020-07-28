# Split and Join


# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

l = 'this is a string boiiiii'


def split_and_join(line):
    return "-".join(line.split(' '))

print(split_and_join(l))
