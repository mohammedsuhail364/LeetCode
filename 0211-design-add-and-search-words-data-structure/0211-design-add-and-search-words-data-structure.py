class WordDictionary:

    def __init__(self):
        self.children={}
        self.isLast=False

    def addWord(self, word: str) -> None:
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=WordDictionary()
            cur=cur.children[c]
        cur.isLast=True

    def search(self, word: str) -> bool:
            root=self
            def dfs(j,cur):
                for i in range(j,len(word)):
                    if word[i]=='.':
                        for c in cur.children.values():
                            if dfs(i+1,c):
                                return True
                        return False
                    else:
                        if word[i] not in cur.children:
                            return False
                        cur=cur.children[word[i]]
                return cur.isLast
            return dfs(0,root)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)