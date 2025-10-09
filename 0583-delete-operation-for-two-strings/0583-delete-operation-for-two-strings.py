class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # similiar to edit distance question
        n,m=len(word1),len(word2)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i==n: # word1 consider as empty so return remain all word2 chars
                return m-j
            if j==m: # word2 consider as empty so return remain all word1 chars
                return n-i
            if word1[i]==word2[j]:
                return dfs(i+1,j+1)
            memo[i,j] = 1+min(dfs(i+1,j),dfs(i,j+1))
            return memo[i,j]
        return dfs(0,0)
        