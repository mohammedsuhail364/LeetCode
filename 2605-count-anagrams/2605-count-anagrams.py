class Solution:
    def countAnagrams(self, s: str) -> int:
        """
        Example: "too"
        Length = 3
        Frequencies = {t:1, o:2}
        formula = 3!/1! * 2!=3
        """
        MOD = 10**9 + 7
        MAX = 100005
        # precompute the factorials
        fact=[1]*MAX
        for i in range(1,MAX):
            fact[i]=(fact[i-1]*i)%MOD
        words=s.split(" ")
        res=1
        for word in words:
            total_len=len(word)
            numerator=fact[total_len]
            denominator=1
            freq=Counter(word)
            for v in freq.values():
                denominator= (denominator*fact[v])%MOD
            
            res*=(numerator*pow(denominator,MOD-2,MOD))
            res=res%MOD
        return res
            