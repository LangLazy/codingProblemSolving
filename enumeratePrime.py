class Solution:
    def enumeratePrimes(self, num: int) -> list[int]:
        if num < 2:
            return []
        elif num == 2:
            return [2]
        else:
            ans = [2]
            for i in range(3,num+1,2):
                if self.primeHuh(i):
                    ans.append(i)
            return ans

    def primeHuh(self, num: int) -> bool:
        i = 2
        while i**2 <= num:
            if num % i == 0:
                return False
            i += 1
        return True

soln = Solution()
print(soln.enumeratePrimes(100))


