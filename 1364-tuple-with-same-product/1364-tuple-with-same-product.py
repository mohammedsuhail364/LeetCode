class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # refer neetcode
        product_cnt=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                product_cnt[product]+=1
        res=0
        for cnt in product_cnt.values():
            pairs=(cnt*(cnt-1))//2
            res+=pairs*8
        return res