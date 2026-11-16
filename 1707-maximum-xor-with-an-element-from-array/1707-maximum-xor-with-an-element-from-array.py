class Trie:
    def __init__(self):
        self.children=[None,None] #(0,1)
    def insert(self,n):
        cur=self
        for i in range(30,-1,-1):
            b = (n>>i)&1 # finds the last bit
            if cur.children[b] is None:
                cur.children[b]=Trie()
            cur=cur.children[b]
class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        # refer this simpler version leetcode NO : 421
        root = Trie()
        nums.sort()
        sorted_queries=sorted([(m,x,i) for i,(x,m) in enumerate(queries)])
        p=0
        res=[-1]*len(queries)
        # for each the sorted queries and add the numbers from nums into trie which is less than m
        for m,x,idx in sorted_queries:
            while p<len(nums) and nums[p]<=m:
                root.insert(nums[p])
                p+=1
            if p==0:continue # which is res[idx]=-1
            cur=root
            xor = 0
            for i in range(30,-1,-1):
                b=(x>>i)&1 #find the last bit
                want = 1 - b # means if b is 1 we get the 0 propably we get the opposite bit
                if cur.children[want]:
                    xor |= (1<<i)
                    cur = cur.children[want]
                else:
                    cur = cur.children[b]
            res[idx]=xor
        return res
        
