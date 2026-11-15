class Trie:
    def __init__(self):
        self.children={}
        self.isLast=False
    def insert(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w]=Trie()
            cur=cur.children[w]
        cur.isLast=True
from collections import deque 


class StreamChecker:

    def __init__(self, words: list[str]):
        self.root=Trie()
        self.max_len=0
        
        for word in words:
            self.root.insert(word[::-1])
            self.max_len=max(self.max_len,len(word))
        self.stream = deque(maxlen=self.max_len)
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        cur=self.root
        for ch in reversed(self.stream):
            if ch not in cur.children:return False
            cur=cur.children[ch]
            if cur.isLast:return True
        return False



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)