class Solution:
    def generate(self, numRows: int):
        res=[[1],[1,1]]
        if numRows<=len(res):
            return res[:numRows]
        i=0
        while i<numRows-2:
            tmp=res[-1]
            nxt=[tmp[0]]
            for x in range(len(tmp)-1):
                val=tmp[x]+tmp[x+1]
                nxt.append(val)
            nxt.append(tmp[-1])
            res.append(nxt)
            i+=1
        return res