class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # check the words from wordDict in the s
        @cache
        def dfs(i):
            if i<0:return True
            for word in wordDict:
                if s[i-len(word)+1:i+1]==word and dfs(i-len(word)):return True
            return False
        return dfs(len(s)-1)