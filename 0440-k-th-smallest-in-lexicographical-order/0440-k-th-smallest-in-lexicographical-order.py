class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur=1
        res=1
        for _ in range(k):
            res=cur
            if cur*10<=n:
                cur*=10
            else:
                if cur>=n:
                    cur//=10
                cur+=1
                while cur%10==0:
                    cur//=10
        return res