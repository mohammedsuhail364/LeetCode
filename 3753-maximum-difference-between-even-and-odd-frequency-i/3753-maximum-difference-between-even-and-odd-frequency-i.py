class Solution:
    def maxDifference(self, s: str) -> int:
        nums=Counter(s)
        q=max((x for x in nums.values() if x%2!=0),default=None)
        q1=min((x for x in nums.values() if x%2==0),default=None)
        return q-q1