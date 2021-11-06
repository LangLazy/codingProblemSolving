class Solution:
    def addingInts(self, number: list[int]) -> list[int]:
        length = len(number)
        for i in reversed(range(length)):
            if (number[i] == 9):
                number[i] = 0
                if i == 0:                    
                    number.append(0)
            else:
                number[i] += 1
                break
        return(number)

soln = Solution()
print(soln.addingInts([9,8,9]))