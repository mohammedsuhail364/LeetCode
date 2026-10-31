class Trie:
    def __init__(self):
        self.children={}
        self.isLast=False

class WordDictionary:

    def __init__(self):
        self.trie=Trie()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur=cur.children[w]
        cur.isLast = True 

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.isLast
            ch = word[i]
            if ch==".":
                # try all paths
                for child in node.children.values():
                    if dfs(child,i+1):return True
                return False
            if ch not in node.children:return False
            return dfs(node.children[ch],i+1)
        return dfs(self.trie,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)