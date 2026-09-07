class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # seen=set()
        # res=0
        # def dfs(i,w):
        #     nonlocal res
        #     if i>=len(s):
        #         if w and w not in seen:
        #             res+=1
        #             seen.add(w)
        #         return
        #     dfs(i+1,w)
        #     dfs(i+1,w+s[i])
        # dfs(0,"")
        # return res
        # to find every subsequence we can reduce by eliminating the redundant subsequence by avoid the duplicate character starting subsequence
        # every subsequence we generate is unique because we eliminate the repeating character starting subsequence 
        MOD = 10**9+7
        cache={}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i>=len(s):
                return 1 # we find the distinct subsequence
            seen=set()
            cache[i]=1
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    cache[i]=(cache[i]+dfs(j+1))%MOD
            return cache[i]

        return (dfs(0)-1)%MOD # remove the empty subsequence
