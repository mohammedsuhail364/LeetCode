class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        i=0
        j=0
        n=len(start)
        while i<n or j<n:
            while i<n and start[i]=='X':
                i+=1
            while j<n and result[j]=='X':
                j+=1
            if (i==n or j==n):
                break
            if start[i]=='R' and i>j:
                return False
            if start[i]=='L' and i<j:
                return False
            i+=1
            j+=1
        return i==n and j==n