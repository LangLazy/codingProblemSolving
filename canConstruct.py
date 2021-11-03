class Solution:
    def canConstruct(self, target, dictionary, memo=None) -> bool:
        if memo is None:
            memo = {}
        if target in memo:
            return memo[target]
        elif target == "":
            return True 
        else:
            for word in dictionary:
                if target.startswith(word):
                    if self.canConstruct(target[len(word):], dictionary, memo):
                        return True
            memo[target] = False
            return False
soln = Solution()
print(soln.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(soln.canConstruct("skateboard", ["bo", "ate", "t", "ska", "sk","boar"]))
print(soln.canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot","o","t"]))
print(soln.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))