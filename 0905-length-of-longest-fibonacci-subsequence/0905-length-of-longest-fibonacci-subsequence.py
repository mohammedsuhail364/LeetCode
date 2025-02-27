class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res=0
        set_arr=set(arr)
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev,cur=arr[i],arr[j]
                nxt=prev+cur
                length=2
                while nxt in set_arr:
                    length+=1
                    prev=cur
                    cur=nxt
                    nxt=prev+cur
                    res=max(res,length)
        return res
