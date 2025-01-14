class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n=A.length;
        int[] res=new int[n];
        int[] cnt=new int[51];
        for (int i=0;i<n;i++){
            cnt[A[i]]++;
            cnt[B[i]]++;
            int newCommon=0;
            if (cnt[A[i]]==2){
                newCommon++;
            }
            if (A[i]!=B[i] && cnt[B[i]]==2){
                newCommon++;
            }
            res[i]=newCommon;
            if(i>0){
                res[i]+=res[i-1];
            }
        }
        return res;

    }
}
