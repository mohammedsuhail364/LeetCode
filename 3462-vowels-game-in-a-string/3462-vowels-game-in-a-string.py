class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels=0
        for i in s:
            if i in 'aeiou':
                vowels+=1
        if vowels==0:
            return False
        if vowels%2:
            return True
        return True