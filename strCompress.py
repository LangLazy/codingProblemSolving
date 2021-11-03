class Solution:
    def strCompress(self, word:str) -> str:
        if word == "":
            return word
        
        og_len = len(word)

        compressed = []

        curChar = word[0]
        curCharCount = 0
        
        for i in range(og_len):
            char = word[i]
            if char == curChar:
                curCharCount += 1
            else:
                compressed.append(curChar)
                compressed.append(str(curCharCount))
                curChar = char
                curCharCount = 1
            
            if i == og_len -1:
                compressed.append(curChar)
                compressed.append(str(curCharCount))

        end = "".join(compressed)
        if og_len > len(end):
            return end
        else:
            return word

sol = Solution()
print(sol.strCompress("aabcccccaaa"))

##Should be O(n + m ) where n is len of original string and m is the length of the compressed string!