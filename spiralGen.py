class Solution:
    def spiralMaker(self, arr:list[list[int]])-> list[int]:
        ans = []
        for i in self.spiralGenerator(len(arr)):
            row =  i // len(arr)
            column = i % len(arr)
            ans.append(arr[row][column])
        return ans
    def spiralGenerator(self, n):
        pads = [0,1,1,2]
        increments = [1,n,-1,-n]
        currentValue = 0
        while min(pads) <= n:
            for i in range(4):
                for _ in range(n - pads[i]):
                    currentValue += increments[i]
                    yield currentValue -1
                pads[i] += 2

soln = Solution()
print(soln.spiralMaker([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
