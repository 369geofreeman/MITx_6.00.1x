class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        nums = {}

        for i,v in enumerate(numbers):
            if target - v in nums:
                return [numbers.index(target-v)+1, i+1]
            else:
                nums[v] = target - v


# -- Tests

def main():
  tests = [
    [2,7,11,15],
    [2,3,4],
    [0,0,3,4],
    [-1,0]
  ]
  targets = [9, 6, 0, -1]
  ans = [
    [1, 2],
    [1, 3],
    [1, 2],
    [1, 2]
  ]
  result = Solution()

  for i in range(len(tests)):
    res = result.twoSum(tests[i], targets[i])
    print('Result:', res)
    print('Answer:', ans[i])
    print('--- correct ---\n') if res == ans[i] else print('--- Wrong---\n')


if __name__ == '__main__':
  main()
