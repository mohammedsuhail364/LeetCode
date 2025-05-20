class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        if(max(nums)>len(queries)):
            return False
        n=len(nums)
        diff=[0]*(n+1)
        for i, j in queries:
            diff[i]+=1
            diff[j+1]-=1
        pre_sum=0
        pre_sum_arr=[0]*n
        for i in range(n):
            pre_sum_arr[i]=pre_sum+diff[i]
            pre_sum=pre_sum_arr[i]
        for i,j in zip(nums,pre_sum_arr):
            if i>j:
                return False
        return True