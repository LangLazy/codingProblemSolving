class Solution:
    def allConstruct(self, target: str, dictionary: list[str], memo=None):
        if memo is None:
            memo={}
        if target in memo:
            return memo[target]
        if target == "":
            return [[]]
        else:
            full_ans = []
            for word in dictionary:
                if target.startswith(word):
                    ans = self.allConstruct(target[len(word):], dictionary, memo) #append on word to get the constructions for the target
                    if ans is not None:
                        for list in ans:
                            list.insert(0, word)
                        full_ans = full_ans + ans
            if full_ans is []:
                return None
            else:
                copy_ans = full_ans.copy()
                for i in range(len(full_ans)):
                    copy_ans[i] = full_ans[i].copy()
                memo[target] = copy_ans
                return full_ans

soln = Solution()
print(soln.allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(soln.allConstruct("skateboard", ["bo", "ate", "t", "ska", "sk","boar"]))
print(soln.allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot","o","t"]))
print(soln.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee"]))
print(soln.allConstruct("skateboard", ["bo", "ate", "t", "ska", "sk","boar"]))

