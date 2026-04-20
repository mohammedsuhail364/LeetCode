class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj=defaultdict(list)
        # this was a tricky problem like if we have a work like hot we can make it *ot,h*t,ho* then we can search to the similiar kind of words 
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                adj[pattern].append(word)
        
        q=deque([(beginWord)])
        visited=set()
        res=1
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res+=1
        return 0
