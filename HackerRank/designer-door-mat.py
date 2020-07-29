# Designer Door Mat


# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# 
# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters




n = 9
m = 27
x = '---'
y = '.|.'


pattern = [(y*(2*i+1)).center(m, '-') for i in range(n//2)]

print("\n".join(pattern), '\n'+ 'WELCOME'.center(m, '-'), '\n' + "\n".join(pattern)[::-1] )

