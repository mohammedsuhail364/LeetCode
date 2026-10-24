class Trie:

    def __init__(self):
        self.children ={}
        self.isLast = False 

    def insert(self, word: str) -> None:
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur=cur.children[w]
        cur.isLast = True
    def search(self, word: str) -> bool:
        cur = self
        for w in word:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        return cur.isLast
    def startsWith(self, prefix: str) -> bool:
        cur = self
        for w in prefix:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)