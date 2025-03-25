class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output=[intervals[0]]
        for s,e in intervals[1:]:
            last_end=output[-1][1]
            if s <= last_end :
                output[-1][1]=max(last_end,e)
            else:
                output.append([s,e])
        return output
        