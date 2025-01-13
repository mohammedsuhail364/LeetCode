class Solution:
    def minimumLength(self, s: str) -> int:
        s=Counter(s)
        total=0
        for i,j in s.items():
            if j%2==0:
                total+=2
            else:
                total+=1
        return total
            
