class Solution:
    def oneChange(self, w1: str, w2: str) -> bool:
        lenString1 = len(w1)
        lenString2 = len(w2)
        if (lenString2 == lenString1):
            seenDif = False
            for i in range(lenString1):
                if w1[i] != w2[i]:
                    if seenDif:
                        return False
                    else:
                        seenDif = True
            return True
        elif abs(lenString1 - lenString2) == 1:
            if lenString1 > lenString2 :
                return self.checkOver(w1, w2)
            else:
                return self.checkOver(w2,w1)
        else:
            return False
    def checkOver(self, large: str, small: str) -> bool:
        shift = 0
        for i in range(len(large) - 1):
            if large[i] != small[i - shift]:
                if shift == 0:
                    shift = 1
                else:
                    return False
        return True
                    

soln = Solution()
print(soln.oneChange("pale", "bake"))