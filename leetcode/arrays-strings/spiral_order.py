class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        if matrix == [] or matrix[0] == []:
          return []

        while matrix != []:
            # Top
            if matrix == [] or matrix[0] == []:
                break
            res.append(matrix[0])
            matrix = matrix[1:]
            print(res)

            # Right
            if matrix == [] or matrix[0] == []:
                break
            res.append([i[-1] for i in matrix])
            matrix = [i[:-1] for i in matrix]

            # Bottom
            if matrix == [] or matrix[0] == []:
                break
            res.append(matrix[-1][::-1])
            matrix = matrix[:-1]

            # Left
            if matrix == [] or matrix[0] == []:
                break
            m = [i[0] for i in matrix]
            res.append(m[::-1])
            matrix = [i[1:] for i in matrix]

        return sum(res,[])



def main():
  matrix = [
            [[1,2,3],[4,5,6],[7,8,9]],
            [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
            [],
            [[],[]],
            [[7],[9],[6]],
            [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
            ]
  Output = [
            [1,2,3,6,9,8,7,4,5],
            [1,2,3,4,8,12,11,10,9,5,6,7],
            [],
            [],
            [7,9,6],
            [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
            ]

  result = Solution()
  for i in range(len(matrix)):
    res = result.spiralOrder(matrix[i])
    print('Result:', res)
    print('Answer:', Output[i])
    print('--- correct ---\n') if res == Output[i] else print('--- Wrong---\n')


if __name__ == '__main__':
  main()
