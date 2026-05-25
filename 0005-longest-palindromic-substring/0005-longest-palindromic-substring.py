class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache={}
        def is_palindrome(i,j):
            if (i,j) in cache:
                return cache[i,j]
            if i>=j:return True # single character or empty 
            if s[i]!=s[j]:return False 
            cache[i,j] = is_palindrome(i+1,j-1)
            return cache[i,j]
        res=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if is_palindrome(i,j) and j-i+1>len(res):
                    res=s[i:j+1]
        return res
