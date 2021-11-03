#stair climbing -> https://leetcode.com/problems/climbing-stairs/submissions/
#Time complexity

#Brute Force:
#O(2^n) time as you have a branch factor of 2 and a maximal tree depth of n (1s subtracted each time)
#O(n) as stack depth is at most n 

#Memoized Soln:
# O(n) as we at most compute n nodes each with at most 2 children 
#O(n) as stack depth is at most n and your memo holds at most n key value pairs so O(n) + O(n) = O(n)
class Solution:
    def climbStairs(self, n: int, memo = None) -> int:
        if memo is None:
            memo = {}
        if n == 2:
            return 2
        elif n == 1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
            return memo[n]
soln = Solution()
print(soln.climbStairs(3))