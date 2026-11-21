class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def isMatches(word):
            j=0
            for ch in word:
                if j<len(pattern) and ch==pattern[j]:
                    j+=1
                elif ch.isupper():
                    return False
            return j==len(pattern)
        return [isMatches(word) for word in queries]