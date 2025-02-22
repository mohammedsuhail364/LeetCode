class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels='aeiou'
        self.res=0
        def backtrack(li,start):
            if len(li)==n:
                self.res+=1
                return
            for x in range(start,len(vowels)):
                li.append(vowels[x])
                backtrack(li,x)
                li.pop()
        
        backtrack([],0)
        return self.res