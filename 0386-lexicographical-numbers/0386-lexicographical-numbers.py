class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        li=[str(i) for i in range(1,n+1)]
        li.sort()
        res=list(map(int,li))
        return res