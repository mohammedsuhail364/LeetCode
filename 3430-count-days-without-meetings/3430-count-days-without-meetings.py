class Solution:
    def countDays(self, days: int, meetings) -> int:
        # refer neet code
        meetings.sort()
        prev_end=0
        for s,e in meetings:
            s=max(s,prev_end+1)
            days-=max(e-s+1,0)
            prev_end=max(prev_end,e)
        return days