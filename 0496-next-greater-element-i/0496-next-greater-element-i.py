class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge={}
        stack =[] # monotonic decreasing 
        for n in nums2:
            while stack and stack[-1]<n:
                tmp=stack.pop()
                nge[tmp]=n # this was the first greater element to this number
            stack.append(n)
        for n in stack: # no greater element 
            nge[n]=-1
        return [nge[n] for n in nums1]
