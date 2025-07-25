class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        freq=Counter(nums)
        subsequence=defaultdict(int)
        for i in nums:
            if freq[i]==0:
                continue
            freq[i]-=1
            if subsequence[i-1]>0:
                subsequence[i-1]-=1
                subsequence[i]+=1
            elif freq[i+1] and freq[i+2]:
                freq[i+1]-=1
                freq[i+2]-=1
                subsequence[i+2]+=1
            else:
                return False
        return True
