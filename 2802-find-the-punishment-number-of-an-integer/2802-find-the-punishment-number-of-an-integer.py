class Solution:
    def punishmentNumber(self, n: int) -> int:
        # check={1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,657,675,703,756,792,909,918,945,964,990,991,999,1000}
        def backtrack(index,cur,target,i_string):
            if index==len(i_string) and cur==target:
                return True
            for j in range(index,len(i_string)):
                if backtrack(j+1,cur+int(i_string[index:j+1]),target,i_string):
                    return True
            return False
        res=0
        for i in range(1,n+1):
            if backtrack(0,0,i,str(i*i)):
                res+=(i*i)
        return res
