class Solution:
    def createPerm(self, lst: list[str], perm: list[int])-> list[str]:
        for i in range(len(lst)):
            while i !=perm[i]:
                lst[i],lst[perm[i]] = lst[perm[i]],lst[i]
                perm[perm[i]], perm[i] = perm[i],perm[perm[i]]
                # v = perm[i]
                # perm[i], perm[perm[i]] = perm[perm[i]],perm[i]
        return lst
soln = Solution()
print(soln.createPerm(["a","b","c","d"], [2,0,1,3]))