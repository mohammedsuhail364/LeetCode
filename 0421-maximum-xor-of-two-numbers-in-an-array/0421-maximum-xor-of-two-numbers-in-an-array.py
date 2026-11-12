class Trie:
    def __init__(self):
        self.children=[None,None]
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # refer striver 
        root = Trie()
        for n in nums:
            cur=root
            for i in range(30,-1,-1):
                b = (n>>i) & 1
                if not cur.children[b]:
                    cur.children[b] = Trie()
                cur=cur.children[b]
        best = 0
        for n in nums:
            cur=root
            xor = 0
            for i in range(30,-1,-1):
                b = (n>>i)&1
                want = 1-b
                if cur.children[want]:
                    xor|=(1<<i)
                    cur = cur.children[want]
                else:
                    cur = cur.children[b]
            best = max(best,xor)
        return best