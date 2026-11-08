class Trie:
    def __init__(self):
        self.children={}
        self.isLast = False
    def insert(self,word):
        cur=self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.isLast = True
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        n=len(s)
        dp = [False]*(n+1)
        dp[n] = True
        for i in range(n-1,-1,-1):
            node = trie
            for j in range(i,n):
                if s[j] not in node.children:
                    break
                node=node.children[s[j]]
                if node.isLast and dp[j+1]:
                    dp[i]=True
                    break
        return dp[0]
