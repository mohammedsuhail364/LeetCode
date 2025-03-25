class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # refer neetcode
        x=[(r[0],r[2]) for r in rectangles]
        y=[(r[1],r[3]) for r in rectangles]
        x.sort()
        y.sort()
        def count_non_overlaps(intervals):
            count=0
            prev_end=-1
            for s,e in intervals:
                if prev_end<=s:
                    count+=1
                prev_end=max(prev_end,e)
            return count
        return max(count_non_overlaps(x),count_non_overlaps(y))>=3