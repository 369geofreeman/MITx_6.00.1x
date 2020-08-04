# Complete-The-Pattern-#6-Odd-Ladder



###Task:
# ---
# 
# You have to write a function pattern which creates the following pattern (see examples) up to the desired number of rows.
# 
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
# 
# If any even number is passed as argument then the pattern should last upto the largest odd number which is smaller than the passed even number.
# 
# ###Examples:
# 
# pattern(9):
# 
# 1
# 333
# 55555
# 7777777
# 999999999
# pattern(6):
# 
# 1
# 333
# 55555




def pattern(n):
    res = ''
    for i in range(1,n+1,2):
        s = str(i)*i
        res += "".join(s)+'\n'
    return res[0:-1]








print(pattern(1))
# "1"
print(pattern(5))
# "1\n333\n55555"
