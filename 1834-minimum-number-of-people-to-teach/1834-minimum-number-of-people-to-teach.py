class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_to_teach=set()
        for i in range(len(friendships)):
            u,v=friendships[i]
            u_language=set(languages[u-1])
            v_language=set(languages[v-1])
            x=u_language.intersection(v_language)
            if x:
                continue
            user_to_teach.add(u)
            user_to_teach.add(v)

        res=inf
        for lan in range(1,n+1):
            count=0
            for user in user_to_teach:
                language=languages[user-1]
                if lan not in language:
                    count+=1
            res=min(res,count)
        return res