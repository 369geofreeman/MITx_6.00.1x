# Find the Runner-Up Score!

# Given the participants' score sheet for your University Sports Day, you are required to find
# the runner-up score. You are given  scores. Store them in a list and find the score of
# the runner-up.


arr = [2, 3, 6, 6, 5]


def listsort(sarr):
    if sarr[-1] != sarr[-2]:
        return sarr[-2]
    else:
        return listsort(sarr[0:-1])


print(listsort(sorted(arr)))
