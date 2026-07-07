class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(reverse=True,key=lambda x:(x[1],-x[0]))
        print(intervals)
        stack=[]
        for s,e in intervals:
            if stack and stack[-1][0]<=s and e<=stack[-1][1]:
                continue
            else:
                stack.append((s,e))
        return len(stack)