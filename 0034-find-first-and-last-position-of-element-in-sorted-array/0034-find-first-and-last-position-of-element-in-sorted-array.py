from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_element_front():
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    res=m
                    r=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return res
        def find_element_back():
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    res=m
                    l=m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return res
        first=find_element_front()
        last=find_element_back()
        return [first,last]