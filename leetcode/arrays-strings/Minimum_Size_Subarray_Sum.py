class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        lb = 0
        ub = 0
        wSum = nums[0]
        numLen = len(nums)
        ans = []
        while lb<numLen:
            # print(lb, ub, wSum)
            if wSum >= target:
                ans.append(ub-lb+1)
            
            if wSum < target and ub+1< numLen:
                ub+=1
                wSum += nums[ub]
            else:
                wSum -= nums[lb]
                lb+=1

        if ans:
            return min(ans)
        return 0
