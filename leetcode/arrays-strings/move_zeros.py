class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        
        for i in range(l):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
        
        return nums
