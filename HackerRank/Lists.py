# coding=utf-8
# Lists

# Consider a list (list = []). You can perform the following commands
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# Pop: pop the last element of the list
# reverse: Reverse the list.
#
#
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


x = []

for i in range(N):
    n = input().split(' ')
    if n[0] == "append":
        x.append(int(n[1]))
    elif n[0] == "insert":
        x.insert(int(n[1]), int(n[2]))
    elif n[0] == "remove":
        x.remove(int(n[1]))
    elif n[0] == "pop":
        x.pop()
    elif n[0] == "sort":
        x.sort()
    elif n[0] == "reverse":
        x.reverse()
    elif n[0] == "print":
        print(x)



