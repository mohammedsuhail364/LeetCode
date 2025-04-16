class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pair_count=0
        res=0
        left=0
        freq=defaultdict(int)
        for right in range(len(nums)):
            pair_count+=freq[nums[right]]
            freq[nums[right]]+=1
            while pair_count>=k:
                res+=len(nums)-right
                pair_count-=freq[nums[left]]-1
                freq[nums[left]]-=1
                left+=1
        return res