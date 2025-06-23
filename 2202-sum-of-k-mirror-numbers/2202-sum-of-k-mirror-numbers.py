class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def create_palidrome(num,odd):
            x=num
            if odd:
                x//=10
            while x>0:
                num=num*10+x%10
                x//=10
            return num
        def is_base_palidrome(num,base):
            digits=[]
            while num>0:
                digits.append(num%base)
                num//=base
            return digits==digits[::-1]
        length=1
        res=0
        while n>0:
            for i in range(length,length*10):
                if n<=0:
                    break
                val=create_palidrome(i,True)
                if is_base_palidrome(val,k):
                    res+=val
                    n-=1
            for i in range(length,length*10):
                if n<=0:
                    break
                val=create_palidrome(i,False)
                if is_base_palidrome(val,k):
                    res+=val
                    n-=1
            length*=10
        return res
