class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res=[]
        amount=sum(nums)

        for i in nums:
            s=i^k
            res.append((s-i))
        print(res)
        res.sort(reverse=True)
        print(res)
        for i in range(0,len(nums),2):
            if i==len(nums)-1:
                break
            ans=res[i]+res[i+1]
            if ans<=0:
                break
            amount+=ans
        return amount     
  