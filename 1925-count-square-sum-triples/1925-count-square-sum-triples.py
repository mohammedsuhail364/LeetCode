class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:
                    k=i**2+j**2
                    if 1<=math.sqrt(k) and math.sqrt(k)<=n and math.sqrt(k)==int(math.sqrt(k)) :
                        c+=1
        return c