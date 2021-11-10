class Solution:
    def buySellStock(self, nums: list[int])-> int:
        maxProfit = 0
        benchmark = nums[0]
        for num in nums:
            if (num - benchmark) > maxProfit:
                maxProfit = num - benchmark
            elif num < benchmark:
                benchmark = num
        return maxProfit

soln = Solution()
print(soln.buySellStock([310,315,275,295,260,270,290,230,255,250]))