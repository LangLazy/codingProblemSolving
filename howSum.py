#How Sum
#Brute Force -> 
# n = number
# m = length of components list
#  Each node has at most m child nodes, and we have at most a height of n as the smalles de-increment is 1
#  So Time is O(m^n*n) as we have at most n levels and a branching factor of m, but also each time we compute we may have to do an array insert which is O(n)
#  Space is O(n) as n is the max recursive depth
# 
# None Brute Force ->
# Space is still O(n^2) ->  as we need the memo which holds at most n keys with corresponding entries of arrays at most n large
# Time is  O(n*m*n) as you have to compute at most n nodes and each one has at most n children, but also at worst we do an inert which is O(n) -> list of all 1s 
class HowSum:
    def howSum(self, number, components, memo = {}) -> list[int]:
        if number in memo:
            return memo[number]
        elif (number == 0):
            return []
        elif (number < 0 ):
            return None
        else:
            for component in components:
                ans = self.howSum(number - component, components, memo)
                if ans is not None:
                    ans.insert(0, component)
                    return ans
                memo[number] = None
            return None

game = HowSum()

print(game.howSum(0,[2,4]))


