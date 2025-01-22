class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                r=n-1
                tar=target-(nums[i]+nums[j])
                while l<r:
                    k=nums[l]+nums[r]
                    if k==tar:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                    elif k<tar:
                        l+=1
                    else:
                        r-=1
        return list(res)
