class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=0
        seen=set()
        if all(n%2 for n in digits):
            return 0
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i==j or not digits[i]:
                    continue
                for k in range(len(digits)):
                    if j==k or i==k:
                        continue
                    e=(digits[i]*100)+(digits[j]*10)+(digits[k])
                    if e%2==0 and e not in seen:
                        seen.add(e)
                        res+=1
        return res