class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        i=n-2
        while True:
            if i>=0 and nums[i]<nums[i+1]:
                break
            if i<0:
                break
            i-=1
        if i>=0:
            j=n-1
            while True:
                if j>=0 and nums[i]<nums[j]:
                    break
                if j<0:
                    break
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=nums[i+1:][::-1]
    

        