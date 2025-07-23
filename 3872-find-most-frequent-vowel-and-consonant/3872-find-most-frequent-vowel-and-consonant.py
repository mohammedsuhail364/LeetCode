class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        vowel=0
        consonant=0
        for i,j in freq.items():
            if i in 'aeiou':
                vowel=max(vowel,j)
            else:
                consonant=max(consonant,j)
        return vowel +consonant