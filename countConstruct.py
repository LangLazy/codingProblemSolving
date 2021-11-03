class Solution:
    def countConstruct(self, target: str, dictionary: list[str], memo=None) -> int:
        if memo is None:
            memo = {}
        if target in memo:
            return memo[target]
        elif target == "":
            return 1
        else:
            total = 0
            for word in dictionary:
                if target.startswith(word):
                    total = total + self.countConstruct(target[len(word):], dictionary, memo)
            memo[target] = total
            return total
soln = Solution()
print(soln.countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(soln.countConstruct("skateboard", ["bo", "ate", "t", "ska", "sk","boar"]))
print(soln.countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot","o","t"]))
print(soln.countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee"]))