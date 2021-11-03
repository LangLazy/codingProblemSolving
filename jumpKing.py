from typing import List


class Solution:
    def canJump(self, nums: List[int], posn=0, memo = None) -> bool:
        if memo is None:
            memo = {}
        if posn in memo:
            return memo[posn]
        elif len(nums) == 1:
            memo[posn] = True
            return True
        elif nums[0] == 0:
            memo[posn] = False
            return False
        else:
            if (len(nums) -1) <= nums[0]:
                return True
            for i in range(1,nums[0]+1):
                if self.canJump(nums[i:], posn + i, memo):
                    memo[posn] = True
                    return True
            memo[posn] = False
            return False
soln = Solution()
gamer = [1,2]
o = gamer[2:]
print(o)