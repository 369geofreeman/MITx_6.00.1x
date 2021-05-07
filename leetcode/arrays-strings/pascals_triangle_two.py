class Solution(object):    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(rowIndex+1):
            result = []
            for j in range(i+1):
                result.append(int(math.factorial(i) / (math.factorial(j) * math.factorial(i-j))))
        return result
