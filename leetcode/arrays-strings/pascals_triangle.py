import math


class Solution(object):
    def binomial_coefficient(self, n, k):
      return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(self.binomial_coefficient(i, j))
            res.append(temp)
        return res


def main():
  result = Solution()
  tests = [1, 5]
  outputs = [
    [[1]],
    [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
  ]

  for i in range(len(tests)):
    res = result.generate(tests[i])
    print('Result:', res)
    print('Answer:', outputs[i])
    print('--- correct ---\n') if res == outputs[i] else print('--- Wrong---\n')


if __name__ == '__main__':
  main()
