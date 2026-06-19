class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre_sum=0
        res=0
        for n in gain:
            pre_sum+=n
            res=max(res,pre_sum)
        return res