class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo={}
        def dfs(a,b):
            if (a,b) in memo:
                return memo[a,b]
            if a==b:
                return True
            if sorted(a)!=sorted(b):
                return False # avoid multiple paths with out wasting
            n=len(a)
            for i in range(1,n):
                # no swap
                if dfs(a[:i],b[:i]) and dfs(a[i:],b[i:]):
                    memo[a,b] = True
                    return memo[a,b]
                # swap compare the a[:i] with b[i+1:] and vice versa
                if dfs(a[:i],b[-i:]) and dfs(a[i:],b[:-i]):
                    memo[a,b] = True
                    return memo[a,b]
            memo[a,b] = False
            return memo[a,b]
        return dfs(s1,s2)