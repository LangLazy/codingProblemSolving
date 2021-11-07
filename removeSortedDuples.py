#My solution for EPI 5.5 - Delete duplicates from sorted array
#Time complexity is O(n) and space is O(1)

class Solution:
    def removeDupes(self, nums: list[int]) -> list[int]:
        maxVal = nums[0]
        freeSpace = 1
        for i in range(1,len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                nums[freeSpace] = nums[i]
                freeSpace += 1
        return nums[:freeSpace]

soln = Solution()
print(soln.removeDupes([1,1,2,2,3,4,4,4,5,6,6,6,7]))

