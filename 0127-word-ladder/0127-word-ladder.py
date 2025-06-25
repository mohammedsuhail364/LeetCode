class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visit=set()
        adj=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                adj[pattern].append(word)
        q=deque([beginWord])
        visit.add(beginWord)
        res=1
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node==endWord:
                    return res
                for j in range(len(node)):
                    pattern=node[:j]+"*"+node[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res+=1
        return 0