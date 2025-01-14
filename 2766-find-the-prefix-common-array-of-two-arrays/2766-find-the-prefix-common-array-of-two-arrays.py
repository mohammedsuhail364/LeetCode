class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[0]*n
        cnt=[0]*51
        for i in range(n):
            cnt[A[i]]+=1
            cnt[B[i]]+=1
            new_common=0
            if cnt[A[i]]==2:
                new_common+=1
            if A[i]!=B[i] and cnt[B[i]]==2:
                new_common+=1
            
            res[i]=new_common
            if i>0:
                res[i]+=res[i-1]
        return res