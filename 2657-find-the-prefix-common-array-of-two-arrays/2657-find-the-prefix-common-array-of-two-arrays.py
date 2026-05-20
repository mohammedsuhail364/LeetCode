from typing import List
from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A_Map=defaultdict(int)
        
        res=[]
        for x in range(len(A)):
            A_Map[A[x]]+=1
            cur=0
            B_Map=defaultdict(int)
            for i in range(x+1):
                B_Map[B[i]]+=1
                if A_Map[B[i]]==B_Map[B[i]]:
                    cur+=1
            res.append(cur)
        return res