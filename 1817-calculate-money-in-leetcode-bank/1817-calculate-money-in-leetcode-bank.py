class Solution:
    def totalMoney(self, n: int) -> int:
        temp=1
        amount=0
        res=0
        for i in range(n):
            if i%7==0:
                temp=1+amount
                amount+=1
            res+=temp
            temp+=1
        return res
