# Implement a recursive version of binary search


def binary_search(x, low, high, arr):
    # Check base case
    if high >= low:

        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(x, low, mid - 1, arr)

        # Else the element can only be present in right subarray
        else:
            return binary_search(x, mid + 1, high, arr)

    else:
        # Element is not present in the array 
        return -1


lst = [i for i in range(100)]
x = 14

# Function call 
result = binary_search(x, 0, len(lst)-1, lst)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
