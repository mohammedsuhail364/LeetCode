class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=len(arr)-1
        # we can shrink the window 
        while (r-l+1)>k:
            # compare the left value with right value
            if abs(arr[l]-x)>abs(arr[r]-x):
                l+=1
            else:
                r-=1
        return arr[l:r+1]