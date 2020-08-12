# Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# Note:
# 
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
#  
# 
# Constraints:
# 
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1.length == m + n
# nums2.length == n



def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2

        x, y = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if x >= 0 and y >= 0:
                if nums1[x] >= nums2[y]:
                    nums1[i] = nums1[x]
                    x -= 1
                else:
                    nums1[i] = nums2[y]
                    y -= 1
            elif x >= 0:
                nums1[i] = nums1[x]
                x -= 1
            else:
                nums1[i] = nums2[y]
                y -= 1

        return nums1



# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m = 3
# n = 3

# nums1 = [0]
# nums2 = [1]
# m = 0
# n = 1

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

print(merge(nums1,m,nums2,n))
