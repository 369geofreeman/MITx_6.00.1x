class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tick = 0
        res = 0

        for i in nums:
            if i == 0:
                tick = 0
            else:
                tick += 1
            if tick > res:
                res = tick
        
        return res
