class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # refer neetcode
        res=0
        cur_max=values[0] - 1 
        for i in range(1,len(values)):
            res=max(res,cur_max+values[i])
            cur_max=max(cur_max-1,values[i]-1)
        return res
        m=0
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                m=max(m,values[i]+values[j]+i-j)
        return m