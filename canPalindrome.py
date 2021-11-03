class Solution:
    def canPalindrome(self, word: str) -> bool:
        word = word.lower()
        if word == "":
            return True
        dict = {}
        for char in word:
            if char.isalpha():
                if char in dict:
                    dict[char] = dict[char] + 1
                else:
                    dict[char] = 1
        seenOdd = False
        sumChars = 0
        for value in dict.values():
            if value % 2 == 1:
                if seenOdd:
                    return False
                else:
                    seenOdd = True
            sumChars += value
        if (sumChars % 2 == 0):
            return not seenOdd
        else:
            return seenOdd

        
sol = Solution()
print(sol.canPalindrome("racecarr"))