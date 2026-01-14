class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=10**9+7
        n=len(arr)
        def findPSEE():
            pse=[-1]*n
            stack=[]
            for i in range(len(arr)):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if stack:
                    pse[i]=stack[-1]
                stack.append(i)
            return pse
            
        def findNSE():
            nse=[n]*n
            stack=[]
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    idx=stack.pop()
                    nse[idx]=i
                stack.append(i)
            return nse
        nse=findNSE()
        pse=findPSEE()
        res=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            res=(res+(arr[i]*left*right)%MOD)%MOD
        return res
