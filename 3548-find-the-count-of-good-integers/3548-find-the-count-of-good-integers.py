class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        n2=(n+1)//2
        seen=set()
        start=10**(n2-1)
        end=10**n2
        res=0
        for v in range(start,end):
            vv=str(v)+str(v)[::-1][n%2:]
            key=''.join(sorted(vv))
            if key not in seen and int(vv)%k==0:
                seen.add(key)
                count=Counter(vv)
                x=(n-count['0'])*math.factorial(n-1)
                for i,c in count.items():
                    x//=math.factorial(c)
                res+=x
        return res
