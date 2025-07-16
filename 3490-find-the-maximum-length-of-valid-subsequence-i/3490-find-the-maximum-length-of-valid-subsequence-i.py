class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # refer https://www.youtube.com/watch?v=VOgE_wdlCAM
        """
        the main observation is we can mod the two values by 2 is always 0 or 1 so we can identify what are the possibilities to get 0 or 1 
        0 -> when the two numbers are odd or two numbers are even so we can make a sequence with this like 1,3,5,7,9 and 2,4,6,8,0
        1 -> when the two numbers are odd and even or even and odd we can make a sequence 
        like 1,2,3,4,5 or 2,3,4,5,6
        so we can check this possibilities and return max of it
        """
        odd,even=0,0
        for n in nums:
            if n%2==0:
                even+=1
            else:
                odd+=1
        odd_start=0
        rem_is_one=True
        for n in nums:
            if n%2==rem_is_one:
                odd_start+=1
                rem_is_one=not rem_is_one # next value should be even
        even_start=0
        rem_is_one=False
        for n in nums:
            if n%2==rem_is_one:
                even_start+=1
                rem_is_one=not rem_is_one # next value should be odd
        return max(odd,even,odd_start,even_start)