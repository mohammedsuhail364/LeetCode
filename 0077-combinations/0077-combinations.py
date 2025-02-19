class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li=[]
        li1=[]
        for i in range(1,n+1):
            li.append(i)
        perm=combinations(li,k)
        for i in perm:
            li1.append(list(i))
        return li1