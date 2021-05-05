class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = min(strs)
        c = ''
        
        for i,v in enumerate(s):
            for j in strs:
                if j[i] != v:
                    return c
            c += v

        return c
