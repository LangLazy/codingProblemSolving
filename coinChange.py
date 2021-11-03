from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int, memo = None) -> int:
        if memo is None:
            memo = {}
        if amount in memo:
            return memo[amount]
        elif amount == 0:
            return 0
        elif amount < 0:
            return -1
        else:
            lowest = -1
            for coin in coins:
                ans = self.coinChange(coins, amount - coin, memo)
                if ans != -1 and (lowest == -1 or (ans + 1) < lowest):
                    lowest = ans +1
            memo[amount] = lowest
            return lowest

soln = Solution()
print(soln.coinChange([1,2,5],100))
