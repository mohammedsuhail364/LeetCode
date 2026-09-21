class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # refer this chat https://claude.ai/share/fb1877b2-bc86-4a4a-baa6-27761cf3e134 by corp account
        # this question basically asks count(subarray of the product % k ) for each index which is not exceed k so return as a array format leave the prefix/suffix explanation
        # brute force is not work there 
        # store the previous remainders and multiply with new num and add in the res
        res=[0]*k
        freq=defaultdict(int)
        for n in nums:
            new_freq=defaultdict(int)
            for rem,cnt in freq.items():
                new_freq[(rem*n)%k]+=cnt
            new_freq[n%k]+=1
            freq=new_freq
            for rem,cnt in freq.items():
                res[rem]+=cnt
        return res
            