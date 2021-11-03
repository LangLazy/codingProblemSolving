class Solution:
    def isPerm(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            dict = {}
            for char in word1:
                if char in dict:
                    dict[char] = dict[char]+1
                else:
                    dict[char] = 1
            for char in word2:
                if char not in dict:
                    return False
                elif dict[char] == 0:
                    return False
                else:
                    dict[char] = dict[char] -1
            for value in dict.values():
                if value != 0:
                    return False
            return True
soln = Solution()
print(soln.isPerm("gamer", "remag"))

