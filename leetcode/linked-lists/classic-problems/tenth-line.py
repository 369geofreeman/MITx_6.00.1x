# tenth-line

# Given a text file file.txt, print just the 10th line of the file.
# 
# Example:
# 
# Assume that file.txt has the following content:
# 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Your script should output the tenth line, which is:
# 
# Line 10


# Option 1 (slowest)
awk 'NR==10' file.txt

# Option 2 (mid)
sed -n 10p file.txt

# option 3 (fastest)
sed '10q;d' file.txt



# 7 / 7 test cases passed.
# Status: Accepted
# Runtime: 0 ms
# Memory Usage: 3.6 MB

# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Tenth Line.
# Memory Usage: 3.6 MB, less than 79.56% of Bash online submissions for Tenth Line
