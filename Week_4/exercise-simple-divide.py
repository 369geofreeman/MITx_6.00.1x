#  Exercise: simple divide


# Suppose we rewrite the FancyDivide function to use a helper function.

# def fancy_divide(list_of_numbers, index):
#    denom = list_of_numbers[index]
#    return [simple_divide(item, denom) for item in list_of_numbers]


# def simple_divide(item, denom):
#    return item / denom


# This code raises a ZeroDivisionError exception for the following call: fancy_divide([0, 2, 4], 0)

# Your task is to change the definition of simple_divide so that the call does not raise an exception.
# When dividing by 0, fancy_divide should return a list with all 0 elements.
# Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers


normalize([0, 0, 0])
