class Trie:
    def __init__(self):
        self.children = {}
        self.word = None
    def insert(self,word)->None:
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w] 
        cur.word = word
    def _dfs(self,node,res)->None:
        if len(res)==3:return
        if node.word is not None:res.append(node.word)
        for child in sorted(node.children):
            if len(res)==3:return
            self._dfs(node.children[child],res)
    def search(self,prefix)->list[str]:
        res=[]
        cur = self
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        self._dfs(cur,res)
        return res

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        trie = Trie()
        res = []
        for word in products:
            trie.insert(word)
        for i in range(len(searchWord)):
            words = trie.search(searchWord[:i+1])
            res.append(words)
        return res
