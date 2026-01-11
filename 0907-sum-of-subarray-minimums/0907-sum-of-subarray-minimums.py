class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # “For every element, count how many subarrays it is the minimum of.”
        MOD=10**9+7
        res=0
        n=len(arr)
        def findNSE():# next smaller element
            stack=[]
            nse=[n]*n
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    idx=stack.pop()
                    nse[idx]=i
                stack.append(i)
            return nse
        def findPSEE(): #previous smaller or equal elements
            stack=[]
            pse=[-1]*n
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if stack:
                    pse[i]=stack[-1]
                stack.append(i)
            return pse
        # refer striver
        pse=findPSEE()
        nse=findNSE()
        for i in range(len(arr)):
            left=i-pse[i]
            right=nse[i]-i
            res=(res+(arr[i]*left*right)%MOD)%MOD
        return res