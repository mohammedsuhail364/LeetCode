class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q=deque(initialBoxes)
        have_key=set()
        visit=set()
        can_open=set()
        res=0
        while q:
            box=q.popleft()
            if box in visit:
                continue
            if status[box] or box in have_key:
                res+=candies[box]
                visit.add(box)
                for key in keys[box]:
                    have_key.add(key)
                    if key in can_open:
                        q.append(key)
                for c in containedBoxes[box]:
                    q.append(c)
            else:
                can_open.add(box)
        return res