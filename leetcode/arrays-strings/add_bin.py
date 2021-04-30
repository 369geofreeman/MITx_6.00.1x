class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return (bin(int(a,2) + int(b,2)))[2:]


def main():
  tests = [
    ['11', '1'],
    ["1010", "1011"]
  ]
  ans = [
    "100",
    "10101"
  ]
  result = Solution()

  for i in range(len(tests)):
    res = result.addBinary(tests[i][0], tests[i][1])
    print('Result:', res)
    print('Answer:', ans[i])
    print('--- correct ---\n') if res == ans[i] else print('--- Wrong---\n')


if __name__ == '__main__':
    main()
