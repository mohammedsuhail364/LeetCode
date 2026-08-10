class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m=len(nums1)
        n=len(nums2)
        # consider this as a 2D Matrix first we can add the (0,0) as this is the minimum of all
        min_heap=[]
        visit=set()
        heappush(min_heap,(nums1[0]+nums2[0],(0,0)))
        visit.add((0,0))
        res=[]
        while k>0 and min_heap:
            val,(i,j)=heappop(min_heap)
            res.append([nums1[i],nums2[j]])
            if i+1<m and (i+1,j) not in visit:
                heappush(min_heap,(nums1[i+1]+nums2[j],(i+1,j)))
                visit.add((i + 1, j))
            if j+1<n and (i,j+1) not in visit:
                heappush(min_heap,(nums1[i]+nums2[j+1],(i,j+1)))
                visit.add((i , j+ 1))
            k-=1
        return res