class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # the first observation is we only consider the absolute difference only 
        d=[]
        for i,j in zip(nums1,nums2):
            d.append(abs(i-j))
        d.sort(reverse=True)
        k=k1+k2
        d.append(0) # just for match the last element
        if k >= sum(d):
            return 0
        for i in range(len(nums1)):
            cost = (d[i]-d[i+1])*(i+1)
            # The key point: i is the index of the current level, and i + 1 is the number of elements we're leveling. You were right to catch the mistake.
            if k>=cost:
                k-=cost
            else:
                q,r = divmod(k,i+1)
                d[:i+1] = [d[i]-q]*(i+1)
                for j in range(r):
                    d[j]-=1
                break
        return sum(x*x for x in d)
