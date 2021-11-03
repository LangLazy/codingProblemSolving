#Can sum

class CanSum:
    def canSum(self,num, components, memo = {}) -> bool:
        if num in memo:
            return memo[num]
        elif (num == 0):
            return True
        elif (num < 0 ):
            return False
        else:
            for number in components:
                if(self.canSum(num-number, components, memo)):
                    return True
                else:
                    memo[num] = False
            return False

game = CanSum()
print(game.canSum(300,[7,14]))