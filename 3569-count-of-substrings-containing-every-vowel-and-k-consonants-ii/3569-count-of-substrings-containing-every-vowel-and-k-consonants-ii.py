class Solution:
    def countOfSubstrings(self, s: str, k: int) -> int:
        # refer neetcode

        def atleast_k(k):
            res=0
            vowels=defaultdict(int)
            non_vowels=0
            l=0
            for r in range(len(s)):
                if s[r] in 'aeiou':
                    vowels[s[r]]+=1
                else:
                    non_vowels+=1
                while len(vowels)==5 and non_vowels>=k:
                    res+=(len(s)-r)
                    if s[l] in 'aeiou':
                        vowels[s[l]]-=1
                    else:
                        non_vowels-=1
                    if vowels[s[l]]==0:
                        vowels.pop(s[l])
                    l+=1
            return res
        return atleast_k(k)-atleast_k(k+1)