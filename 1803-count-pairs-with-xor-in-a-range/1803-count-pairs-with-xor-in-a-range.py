class Trie:
    def __init__(self):
        self.children=[None,None]
        self.count = 0
    def insert(self,n):
        cur=self
        for i in range(15,-1,-1):
            num_bit = (n>>i)&1
            if cur.children[num_bit] is None:
                cur.children[num_bit]=Trie()
            cur = cur.children[num_bit]
            cur.count+=1
    def count_xor_less_than(self,n,limit):
        cur=self
        total=0
        for i in range(15,-1,-1):
            num_bit = (n>>i)&1
            limit_bit = (limit>>i)&1
            if limit_bit ==1:
                if num_bit==0:
                    # add the same sign
                    if cur.children[0]:
                        total+=cur.children[0].count
                    cur=cur.children[1]
                else:
                    # add the same sign
                    if cur.children[1]:
                        total+=cur.children[1].count
                    cur=cur.children[0]
            else:
                cur=cur.children[num_bit]
            if cur is None:break
        return total
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # while insertion the binary into trie is same 
        # but finding the values which low<=val<=high is to find with a trick
        # we have provision only finds the elements which is less than the given values 
        # so first we find the (high+1) counts then it involves the low also 
        # then find the less than low values then subtract into high + 1
        # we findout the inbetween the values
        res=0
        trie=Trie()
        for n in nums:
            query=trie.count_xor_less_than(n,high+1)-trie.count_xor_less_than(n,low)
            res+=query
            trie.insert(n)
        return res