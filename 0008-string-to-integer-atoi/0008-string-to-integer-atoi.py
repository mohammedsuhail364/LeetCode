class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0
        i=0
        res=""
        sign=''
        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s)  and s[i] in ['-','+']:
            sign=s[i]
            i+=1
        while i<len(s) and s[i]=="0":
            i+=1
        while i<len(s) and s[i] in "1234567890":
            res+=s[i]
            i+=1
        res=0 if res=="" else sign+res
        res=int(res)
        if res>(2**31)-1:
            return (2**31)-1
        if res < -(2**31):
            return -(2**31)
        return res

        
        
