# Defanging an IP Address


# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# 
# A defanged IP address replaces every period "." with "[.]".
# 
#  
# 
# Example 1:
# 
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
# 
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"



def defangIPaddr(address):
    return address.replace('.','[.]')


print(defangIPaddr("255.100.50.0"))




# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.7 MB
