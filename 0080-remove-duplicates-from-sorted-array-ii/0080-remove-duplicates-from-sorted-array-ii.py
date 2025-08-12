class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        res=[]
        for i in nums:
            if freq[i]<2:
                res.append(i)
            freq[i]+=1
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)