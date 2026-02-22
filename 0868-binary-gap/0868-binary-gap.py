class Solution:
    def binaryGap(self, n: int) -> int:
        bin_val=bin(n)[2:]
        index_of_ones=[]
        for i in range(len(bin_val)):
            if bin_val[i]=='1':
                index_of_ones.append(i)
        print(index_of_ones)
        if len(index_of_ones)==1:
            return 0
        l=0
        res=0
        for r in range(len(index_of_ones)):
            if (r-l+1)>2:
                l+=1
            if (r-l+1)==2:
                res=max(res,index_of_ones[r]-index_of_ones[l])
        return res
        
