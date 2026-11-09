from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))        # virtual indices (already a valid heap)
        busy = []                    # (end_time, server_id)
        cnt = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            # release finished servers
            while busy and busy[0][0] <= a:
                _, s = heappop(busy)
                heappush(free, i + (s - i) % k)

            # fix stale virtual indices (< i) by moving them to the next lap
            while free and free[0] < i:
                v = heappop(free)
                heappush(free, v + ((i - v + k - 1) // k) * k)

            if not free:             # all busy -> dropped
                continue

            s = heappop(free) % k
            cnt[s] += 1
            heappush(busy, (a + l, s))

        mx = max(cnt)
        return [s for s in range(k) if cnt[s] == mx]