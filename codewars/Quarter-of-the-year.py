# Quarter of the year



# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# 
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.


def quarter_of(month):
    if month < 4: return 1
    if month < 7: return 2
    if month < 10: return 3
    return 4


print(quarter_of(3))
print(quarter_of(4))
print(quarter_of(8))
print(quarter_of(12))
