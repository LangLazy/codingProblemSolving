#Sieve soln for the enumerate primes problem in EPI pg52, the time complexity is O(nlog(log n)) and space is O(n)
#This is better than the regular divsion checker solution
class Solution: 
    def enumeratePrimesSieve(self, num:int) -> list[int]:
        if num < 2:
            return []
        else:
            ans = []
            sieve = [False]*2 + [True]*(num - 1)
            for i in range(num+1):
                if sieve[i]:
                    ans.append(i)
                    for i in range(i, num+1, i):
                        sieve[i] = False
            return ans

soln = Solution()
print(soln.enumeratePrimesSieve(100))

 