class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        n=len(s)
        tree=[None]*(4*n) # (pref,suf,best,lc,rc,length) we can store in the tree for the respective index
        def build(node,l,r):
            if l==r:
                tree[node]=(1,1,1,s[l],s[r],1)
                return
            mid=(l+r)//2
            build(2*node,l,mid)
            build(2*node+1,mid+1,r)
            tree[node]=merge(tree[2*node],tree[2*node+1])
        def merge(L,R):
            left_pref,left_suf,left_best,left_lc,left_rc,left_len=L
            right_pref,right_suf,right_best,right_lc,right_rc,right_len=R
            length=left_len+right_len
            lc=left_lc
            rc=right_rc
            cur_best=max(left_best,right_best)
            boundry_run= left_suf+right_pref if left_rc==right_lc else 0
            best=max(cur_best,boundry_run)
            if left_len==left_pref and left_rc==right_lc:
                prefix_run = left_pref + right_pref
            else:
                prefix_run=left_pref
            if right_len==right_suf and left_rc == right_lc:
                suffix_run = left_suf + right_suf
            else:
                suffix_run = right_suf
            return (prefix_run,suffix_run,best,lc,rc,length)

        def update(node,l,r,idx):
            if l==r:
                tree[node]=(1,1,1,s[l],s[r],1)
                return
            mid=(l+r)//2
            if idx<=mid:
                update(2*node,l,mid,idx)
            else:
                update(2*node+1,mid+1,r,idx)
            tree[node]=merge(tree[2*node],tree[2*node+1])


        res=[]
        build(1,0,n-1)
        for ch,idx in zip(queryCharacters,queryIndices):
            s[idx] = ch
            update(1,0,n-1,idx)
            res.append(tree[1][2])
        return res

