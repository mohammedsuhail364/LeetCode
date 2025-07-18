class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        secret=list(secret)
        guess=list(guess)
        gue=defaultdict(int)
        sec=defaultdict(int)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                secret[i]=guess[i]=""
            else:
                sec[secret[i]]+=1
                gue[guess[i]]+=1
        cows=0
        for i in sec:
            cows+=min(sec[i],gue[i])
        return f"{bulls}A{cows}B"
        