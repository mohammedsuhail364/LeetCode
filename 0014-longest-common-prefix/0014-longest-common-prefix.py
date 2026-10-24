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
    def findPrefix(self):
        cur = self
        res=[]
        while len(cur.children)==1 and not cur.isLast:
            ch,cur = next(iter(cur.children.items()))
            res.append(ch)
        return "".join(res) 
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        words = Trie()
        for word in strs:
            if word=="":
                return ""
            words.insert(word)
        return words.findPrefix()
        