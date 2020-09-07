# recursion-palindrome

# Write a recursive call to check if a striung is a palindrome



def is_palindrome(s):
    if type(s) != str: return print('please use a string!')
    if len(s) <=1:
        return True
    else:
        if s[0].lower() == s[len(s)-1].lower():
            return is_palindrome(s[1:len(s)-1])
        else:
            return False


print(is_palindrome('Sarah'))
# >>> False
print(is_palindrome('racecar'))
# >>> True
print(is_palindrome('Racecar'))
# >>> True
print(is_palindrome('a'))
# >>> True
print(is_palindrome('ab'))
# >>> False
print(is_palindrome('aa'))
# >>> True
print(is_palindrome(66))
# >>> Please use a string!
