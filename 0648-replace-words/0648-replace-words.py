class Trie:
    def __init__(self):
        self.children={}
        self.word = None
    def insert(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w]= Trie()
            cur = cur.children[w]
        cur.word=word
    def search(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                if cur.word:return cur.word
                return word
            if cur.word:return cur.word
            cur = cur.children[w]
        return word

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        res=sentence.split(" ")
        for i in range(len(res)):
            word=res[i]
            replace_word = trie.search(word)
            res[i]=replace_word
        print(res)
        return ' '.join(res)