class Solution:
    def sumZero(self, n: int) :
        res=[]
        i=0
        while len(res)<n:
            if i==0:
                res.append(i)
            else:
                res.append(i)
                res.append(-i)
            i+=1
        return res if len(res)==n else res[1:]