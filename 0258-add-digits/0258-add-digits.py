class Solution:
    def addDigits(self, num: int) -> int:

        while int(num)>9:
            total=0
            s=str(num)
            for i in s:
                total+=int(i)
            num=total
        return num
        
        