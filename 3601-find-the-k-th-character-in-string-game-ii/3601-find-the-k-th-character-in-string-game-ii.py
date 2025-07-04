class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # one again to watch 
        count=0
        val=k
        while val>1:
            jump=math.ceil(math.log2(val))
            val-=2**(jump-1)
            count+=operations[jump-1]
        return chr(ord('a')+(count%26))