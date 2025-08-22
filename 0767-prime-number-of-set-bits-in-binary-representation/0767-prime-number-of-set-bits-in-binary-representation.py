class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_nums=[True]*35
        prime_nums[0]=prime_nums[1]=False
        for i in range(2,int(len(prime_nums)**0.5)+1):
            x=i+i
            if prime_nums[i]:
                for x in range(i*i,len(prime_nums), i):
                    prime_nums[x]=False
        res=0
        for i in range(left,right+1):
            tmp=bin(i).count("1")
            if prime_nums[tmp]:
                res+=1
        return res
