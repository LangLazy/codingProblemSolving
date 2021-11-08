class Solution:
    def twoSum(self, nums: list[int], target: int)-> list[int]:
        memo ={}
        nums.sort
        for i in range(len(nums)):
            memo[target - nums[i]] = i
        for i in range(len(nums)):
            if (nums[i] in memo) and (i !=memo[nums[i]]) :
                return [i, memo[nums[i]]]

soln = Solution()
print(soln.twoSum([2,7,11,15], 9))
             