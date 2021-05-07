class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(' ')
        a = [i.strip() for i in a if i]
        return ' '.join(a[::-1])
