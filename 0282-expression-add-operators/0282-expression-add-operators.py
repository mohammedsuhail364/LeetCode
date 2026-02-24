class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n=len(num)
        res=[]
        def dfs(index,val,last,path):
            if index==n:
                if val==target:
                    res.append(path)
                return
            for i in range(index,n):
                if i>index and num[index]=='0':
                    break
                cur_str=num[index:i+1]
                cur=int(cur_str)
                if index==0: # no operand before
                    dfs(i+1,cur,cur,cur_str)
                else:
                    # addition
                    dfs(i+1,val+cur,cur,path+'+'+cur_str)
                    # subtraction
                    dfs(i+1,val-cur,-cur,path+'-'+cur_str)
                    # multiply
                    dfs(i+1,val-last+last*cur,last*cur,path+'*'+cur_str)
        dfs(0,0,0,"")
        return res