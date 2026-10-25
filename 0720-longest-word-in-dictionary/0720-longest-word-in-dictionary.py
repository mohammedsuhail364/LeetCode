class Trie:
    def __init__(self):
        self.children={}
        self.isLast = False
    def insert(self,word)->None:
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.isLast = True
    def find(self)->str:
        res=""
        q=deque([(self,"")])
        while q:
            node,word = q.popleft()
            if len(word)>len(res) or (len(word)==len(res) and word<res):
                res=word
            for ch,child in node.children.items():
                if child.isLast:
                    q.append((child,word+ch))
        return res
class Solution:
    def longestWord(self, words: list[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.find()
        