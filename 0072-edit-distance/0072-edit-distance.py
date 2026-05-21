class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache={}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[i,j]
            if j>=len(word2): # when j exceeds but i has a value we want to delete the chars in word1
                return len(word1)-i
            if i>=len(word1): # when i exceeds but j has a value we want to insert the chars in word1
                return len(word2)-j
            if word1[i]==word2[j]:
                cache[i,j] = dfs(i+1,j+1)
                return cache[i,j]
            insert=1+dfs(i,j+1)
            delete=1+dfs(i+1,j)
            replace=1+dfs(i+1,j+1)
            cache[i,j] = min(insert,delete,replace)
            return cache[i,j]
        return dfs(0,0)