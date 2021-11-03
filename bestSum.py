#How Sum
#Brute Force -> 

class BestSum:
    def bestSum(self, number, components, memo=None) -> list[int]:
        if memo is None:
            memo = {}
        if number == 0:
            return []
        elif number < 0:
            return None
        elif number in memo:
            if memo[number] is None:
                return None
            else:
                return memo[number].copy()
        else:
            ans = None
            for component in components:
                curAns = self.bestSum(number - component, components,memo)
                if curAns != None and (ans == None or (len(curAns) + 1) < len(ans)):
                    ans = curAns
                    ans.insert(0, component)
            if ans is not None:
                memo[number] = ans.copy()
            else:
                memo[number] = None
            return ans



game = BestSum()

print(game.bestSum(8,[2,3,5]))
print(game.bestSum(8,[1,4,5]))
print(game.bestSum(100,[1,2,5,10,25]))



