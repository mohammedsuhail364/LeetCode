class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            num=list(str(num))
            num.sort()
            c=0
            while num[0]=='0':
                c+=1
                num.pop(0)
            for i in range(c):
                num.insert(1,'0')
            return int(''.join(num))
        else:
            num=list(str(num))
            num.sort(reverse=True)
            k=num.pop()
            num.insert(0,k)
            return int(''.join(num))