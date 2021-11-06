class Solution:
    def rotate90(self, matrix:list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        numLayers = n // 2
        rowSize = n
        for i in range(numLayers):
            onShift = 0
            for x in range(rowSize-1):
                # topLeft = (i,i + x)
                # topRight = (i+x,n -1 -i)
                # bottomLeft = (n - 1 - i  - x,i)
                # bottomRight = (n - 1 - i, n -1 -i -x)
                temp = matrix[i+x][n -1 -i]
                matrix[i+x][n -1 -i] = matrix[i][i + x] #give top right the value of top left
                temp, matrix[n - 1 - i][n -1 -i -x] = matrix[n - 1 - i][n -1 -i -x], temp #switch top right with bottom right
                temp, matrix[n - 1 - i  - x][i] = matrix[n - 1 - i  - x][i], temp #switch bottom right with bottom left
                matrix[i][i + x] = temp
            rowSize = rowSize - 2
        return matrix

soln = Solution()
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(soln.rotate90(arr))
