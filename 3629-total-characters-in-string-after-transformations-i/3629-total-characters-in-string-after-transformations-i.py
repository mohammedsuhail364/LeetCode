class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26
        for i in s:
            cnt[ord(i) - ord("a")] += 1
        for i in range(t):
            tmp = [0] * 26
            for x in range(26):
                if x == 25:
                    tmp[0] = (tmp[0] + cnt[x]) % MOD
                    tmp[1] = (tmp[1] + cnt[x]) % MOD
                else:
                    tmp[x + 1] = (tmp[x + 1] + cnt[x]) % MOD
            cnt = tmp
        return sum(cnt) % MOD
