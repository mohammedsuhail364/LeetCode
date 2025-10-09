class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i==len(word1): # word1 becomes empty
                return len(word2)-j
            if j==len(word2): # word2 becomes empty
                return len(word1)-i
            if word1[i]==word2[j]:
                return dfs(i+1,j+1)
            insert=dfs(i,j+1)
            delete=dfs(i+1,j)
            replace=dfs(i+1,j+1)
            memo[i,j]=1+min(insert,delete,replace)
            return memo[i,j]
        return dfs(0,0)