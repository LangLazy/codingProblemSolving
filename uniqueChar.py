class Solution:
    def uniqueChar(self, word: str, hash: dict = None) -> bool:
        if len(str) > 128:
            return False
        if hash is None:
            hash = {}
        for char in word:
            if char in hash:
                return False
            else:
                hash[char] = True
        return True

soln = Solution()
print(soln.uniqueChar("gamerm"))
