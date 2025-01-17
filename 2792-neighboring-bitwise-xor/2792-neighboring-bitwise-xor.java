class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int first=0;
        int last=0;
        for (int n:derived){
            if (n==1){
                last=~last;
            }
        }
        return first==last;
    }
}