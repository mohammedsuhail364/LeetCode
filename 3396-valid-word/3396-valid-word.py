class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel=0
        consonant=0
        for w in word:
            w=w.lower()
            if w in 'aeiou':
                vowel+=1
            elif w in '1234567890':
                continue
            elif w in "qwrtypsdfghjklzxcvbnm":
                consonant+=1
            else:
                return False
        if vowel and consonant:
            return True
        return False