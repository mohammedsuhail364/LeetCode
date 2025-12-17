class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # first we can find the subarrays which has less than or equal to k unique elements which is easy
        # then we can find the subarrays which has only less than k unique elements which is also easy but reverse thinking like less than only means subarrays < k == subarrays <= k-1 which both are same but right part is easy to find with the same helper function
        def good_subarrays(nums,k):
            res=0
            l=0
            freq=defaultdict(int)
            for r in range(len(nums)):
                freq[nums[r]]+=1
                while len(freq)>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                res+=(r-l+1) # which tells if r and l comes after the while means only subarray contain less than or equal to k unique elements that time we can include it 
                # for example k=2 then arr=[1,2,1]
                # at r = 1 then we can already calculate the first sub array so we can calculate at this point are (1-0)+1 that time is 2 it indicates [1,2] and [2].
            return res
        return good_subarrays(nums,k)-good_subarrays(nums,k-1)