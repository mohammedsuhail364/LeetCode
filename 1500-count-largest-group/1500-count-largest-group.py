class Solution:
    def countLargestGroup(self, n: int) -> int:
        di=defaultdict(int)
        for i in range(1,n+1):
            temp=0
            while i:
                temp+=(i%10)
                i=i//10
            di[str(temp)]+=1
        l_group=max(di.values())
        res=0
        for i,j in di.items():
            if j==l_group:
                res+=1
        return res