class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            prev=res.pop()
            cur=intervals[i]
            if prev[-1]>=cur[0]:
                res.append([prev[0],max(prev[-1],cur[-1])])
            else:
                res.append(prev)
                res.append(cur)
        return res