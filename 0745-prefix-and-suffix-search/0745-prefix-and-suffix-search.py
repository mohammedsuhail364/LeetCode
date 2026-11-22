class Trie:
    def __init__(self):
        self.children={}
        self.index = -1
    def insert(self,word,idx):
        cur = self
        for i,w in enumerate(word):
            if w not in cur.children:
                cur.children[w]=Trie()
            cur=cur.children[w]
            cur.index = idx
    def query(self,word):
        cur=self
        for w in word:
            if w not in cur.children:return -1
            cur=cur.children[w]
        return cur.index
class WordFilter:
    # refer notes
    def __init__(self, words: list[str]):
        self.trie = Trie()
        for idx,word in enumerate(words):
            for k in range(len(word)):
                self.trie.insert(word[k:]+"#"+word,idx)
    def f(self, pref: str, suff: str) -> int:
        return self.trie.query(suff + "#" + pref)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)