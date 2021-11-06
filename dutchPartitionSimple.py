class Solution:
    def dutchPartionNaive(self, nums: list[int], pivot: int) -> list[int]:
        smallerThan = []
        amtSame = 0
        largerThan = []
        pivotVal = nums[pivot]
        for num in nums:
            if num < pivotVal:
                smallerThan.append(num)
            elif num == pivotVal:
                amtSame +=1
            else:
                largerThan.append(num)
        return smallerThan + [pivotVal]*amtSame + largerThan

soln = Solution()
print(soln.dutchPartionNaive([0,1,2,0,2,1,], 2))
