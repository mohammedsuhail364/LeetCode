class Trie:
    def __init__(self):
        self.children={}
        self.isLast=False
    def add_word(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=Trie()
            cur=cur.children[c]
        cur.isLast=True


                
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first add the words as Trie
        root=Trie()
        res=set()
        visited=set()
        for word in words:
            root.add_word(word)
        def dfs(r,c,node,word):
            if r<0 or c<0 or c==COLS or r==ROWS or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isLast:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))
        ROWS=len(board)
        COLS=len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)

        