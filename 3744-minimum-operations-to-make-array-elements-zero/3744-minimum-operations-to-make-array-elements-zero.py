class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # refer this => https://www.youtube.com/watch?v=H2qILXYobSk
        res=0
        for start,end in queries:
            prev=1
            ops=0
            for d in range(1,17):
                cur=prev*4
                l=max(start,prev)
                r=min(end,cur-1)
                if r>=l:
                    ops+=((r-l+1)*d)
                prev=cur
            res+=(ops+1)//2
        return res