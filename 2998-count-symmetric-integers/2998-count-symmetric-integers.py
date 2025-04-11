class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            val=str(i)
            if len(val)%2:
                continue
            div=len(val)//2
            n1=0
            for x in range(div):
                n1+=int(val[x])
            n2=0
            for x in range(div,len(val)):
                n2+=int(val[x])
            if n1==n2:
                c+=1
        return c
