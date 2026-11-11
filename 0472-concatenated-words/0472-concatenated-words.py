class Trie:
    def __init__(self):
        self.children={}
        self.isLast = False
    def insert(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.isLast = True
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        def canForm(word):
            n=len(word)
            memo = {}
            def dfs(i):
                if i==n:return True
                if i in memo:return memo[i]
                res=False
                cur=trie
                for j in range(i,n):
                    ch=word[j]
                    if ch not in cur.children:break
                    cur=cur.children[ch]
                    if cur.isLast:
                        if i==0 and j==n-1: # means it was a single word, we need 1+ words 
                            continue
                        if dfs(j+1):
                            res=True
                            break
                memo[i]=res
                return memo[i] 
            return dfs(0)
        
        return [w for w in words if canForm(w)]