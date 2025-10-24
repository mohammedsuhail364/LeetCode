class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i=n+1
        def is_balanced(i):
            temp=i
            freq=defaultdict(int)
            while temp:
                rem=temp%10
                freq[rem]+=1
                temp=temp//10
            for i,j in freq.items():
                if i!=j:
                    return False
            return True
        while True:
            if is_balanced(i):
                return i
            i+=1
        