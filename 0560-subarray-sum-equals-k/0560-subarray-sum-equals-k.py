class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di=defaultdict(int)
        di[0]=1
        cur_sum=0
        res=0
        for i in nums:
            cur_sum+=i
            remove=cur_sum-k
            if remove in di:
                res+=di[remove]
            di[cur_sum]+=1
        return res