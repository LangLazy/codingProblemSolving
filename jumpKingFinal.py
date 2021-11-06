class Solution:
    def jumpKing(self, nums: list[int]) -> bool:
        stepsLeft = nums[0]
        if stepsLeft >= len(nums) - 1:
            return True
        for i in range(len(nums)):
            if nums[i] > stepsLeft:
                if nums[i] >= (len(nums) -1 -i):
                    return True
                stepsLeft = nums[i] -1
            else:
                stepsLeft -= 1
                if stepsLeft < 0:
                    return False

# class Solution:
#     def jumpKing(self, nums: list[int]) -> bool:
#         if nums[0] >= (len(nums) -1):
#             return True
#         else:
#             maxSkip = nums[0]
#             for i in range(1,nums[0]+1):
#                 if nums[i] + i > maxSkip:
#                     return self.jumpKing(nums[i:])
#             return False

soln = Solution()
print(soln.jumpKing([1,2,3]))