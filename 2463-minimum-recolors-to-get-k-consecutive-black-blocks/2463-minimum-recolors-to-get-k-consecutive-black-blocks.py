class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        j=k
        res=float('inf')
        while j<=len(blocks):
            block=blocks[i:j]
            if block.count('B')==k:
                return 0
            res=min(block.count('W'),res)
            i+=1
            j+=1
        return res
            
            
