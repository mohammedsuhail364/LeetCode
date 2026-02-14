class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this question was very interesting 
        # always remember permutation always looks like this 123 < 132 < 213 < 231 < 312 < 321
        # increasing order
        # if we want to find after the last one we want to return first one 
        # simple trick happend there 
        # eg : 2154300
        # 1. find the non decreasing order from backwards
        # 2. swap the smallest one after the break
        # 3. reverse the slicing part
        n=len(nums)
        i=n-2
        while True:
            if i<0 or (i>=0 and nums[i]<nums[i+1]):
                break
            i-=1
        if i>=0:
            j=n-1
            # find the smallest one after that break point
            while True:
                if j<0 or (j>=0 and nums[i]<nums[j]):
                    break
                j-=1
            # swap the small number after the break point and break point
            nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=nums[i+1:][::-1]