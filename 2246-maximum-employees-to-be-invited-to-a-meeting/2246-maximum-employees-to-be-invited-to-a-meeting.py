class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # refer neetcode
        """
        observation lead to solution:
        -----------------------------
        1)Every connected component has exactely one cycle
        2)components with a cycle of length = 2 ,form non closed circle.
        they can be connected to other non closed circles.
        3)components with a cycle of length > 2, form  closed circles.
        They can't connected.

        To find :
        ---------
        1) Find the longest cycle that means longest closed circle cycle.
        2) Find all components with length =2 cycles. For each , find the 
        longest path in the component and sum all of the paths.
        3)Return max of step 1 and step 2.
        
        """

        # 1) find the longest cycle 

        n=len(favorite)
        visit=[False]*n
        longest_cycle=0
        length_2_cycles=[]
        for i in range(n):
            if visit[i]:
                continue
            start,cur=i,i
            cur_set=set()
            while not visit[cur]:
                visit[cur]=True
                cur_set.add(cur)
                cur=favorite[cur]
            # if cur in cur_set:
            length=len(cur_set)
            while start != cur:
                length-=1
                start=favorite[start]
            longest_cycle=max(longest_cycle,length)
            if length==2:
                length_2_cycles.append([cur,favorite[cur]])
        # 2)Find sum of longest non closed cycles
        
        inverted=defaultdict(list)
        for dst,src in enumerate(favorite):
            inverted[src].append(dst)
        def bfs(src,parent):
            q=deque([(src,0)]) # node,length
            max_length=0
            while q:
                node,length=q.popleft()
                if node==parent:
                    continue
                max_length=max(max_length,length)
                for nei in inverted[node]:
                    q.append((nei,length+1))
            return max_length
        chain_sum=0
        for n1,n2 in length_2_cycles:
            chain_sum+=bfs(n1,n2)+bfs(n2,n1)+2
        return max(chain_sum,longest_cycle)


            


