class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        maxCommon=0
        res=[0]*len(A)
        for i in range(len(A)):
            new_a=A[:i+1]
            new_b=B[:i+1]
            temp=0
            for x in new_a:
                if x in new_b:
                    temp+=1
            res[i]=temp
                    
        return res