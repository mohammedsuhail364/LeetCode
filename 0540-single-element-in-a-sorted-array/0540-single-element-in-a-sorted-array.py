class Solution:
    def singleNonDuplicate(self, nums) -> int:
        # EXPLANATION:-
        # Suppose array is [1, 1, 2, 2, 3, 3, 4, 5, 5]
        # we can observe that for each pair, 
        # first element takes even position and second element takes odd position
        # for example, 1 is appeared as a pair,
        # so it takes 0 and 1 positions. similarly for all the pairs also.

        # this pattern will be missed when single element is appeared in the array.

        # From these points, we can implement algorithm.
        # 1. Take left and right pointers . 
        #     left points to start of list. right points to end of the list.
        # 2. find mid.
        #     if mid is even, then it's duplicate should be in next index.
        #     or if mid is odd, then it's duplicate  should be in previous index.
        #     check these two conditions, 
        #     if any of the conditions is satisfied,
        #     then pattern is not missed, 
        #     so check in next half of the array. i.e, left = mid + 1
        #     if condition is not satisfied, then the pattern is missed.
        #     so, single number must be before mid.
        #     so, update end to mid.
        # 3. At last return the nums[left]
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if (m%2==1 and nums[m-1]==nums[m]) or (m%2==0 and nums[m]==nums[m+1]):
                l=m+1
            else:
                r=m
        return nums[l]
