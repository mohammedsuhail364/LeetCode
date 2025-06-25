class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/solutions/6881305/beginner-freindly-java-c-python-js/?envType=daily-question&envId=2025-06-25
        nums1.sort()
        nums2.sort()
        def count_pairs(x):
            count=0
            for a in nums1:
                if a>0:
                    # a*b<=x then b<=x//a
                    b=x//a
                    count+=(bisect_right(nums2,b)) # in this we can easily find how many value less than b in nums2
                elif a<0:
                    # safely handle negatives
                    # -a*b<=x then b<=-(x//a) -> we can remove the negative less than changes to greater than eg : -3 * b <= 6 then b becomes always higher in this case -2 
                    b=x//a
                    # in this case we can find greater than b so find asusal like a then we can subtract that value from nums2
                    if x%a!=0:
                        b+=1 # ceil the number
                    count+= len(nums2)-(bisect_left(nums2,b)) 
                else:
                    if x>=0:
                        count+=len(nums2)
            return count
        low=-10**10
        high=10**10
        while low<high:
            mid=(low+high)//2
            if count_pairs(mid)<k:
                low=mid+1
            else:
                high=mid
        return low