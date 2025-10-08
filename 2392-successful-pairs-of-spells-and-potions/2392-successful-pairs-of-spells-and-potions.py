class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n=len(potions)
        def binary_search(val):
            l=0
            r=len(potions)-1
            best=n # default not found
            while l<=r:
                m=(l+r)//2
                if (potions[m]*val)>=success:
                    best=m
                    r=m-1
                else:
                    l=m+1
            return best
        res=[]
        potions.sort()
        for i in spells:
            j=binary_search(i)
            res.append(n-j)
        return res