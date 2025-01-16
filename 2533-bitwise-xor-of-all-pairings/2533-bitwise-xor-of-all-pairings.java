class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int res=0;
        if ((nums1.length)%2==1){
            for (int m:nums2){
                res^=m;
            }
        }
        if ((nums2.length)%2==1){
            for(int n:nums1){
                res^=n;
            }
        }
        return res;
    }
}