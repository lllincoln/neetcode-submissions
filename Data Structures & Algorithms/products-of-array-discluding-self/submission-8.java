class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ltr = new int[nums.length + 2];
        int[] rtl = new int[nums.length + 2];
        ltr[0] = 1;
        ltr[ltr.length - 1] = 1;
        rtl[0] = 1;
        rtl[rtl.length - 1] = 1;

        for (int i = 0; i < nums.length; i++) {
            ltr[i + 1] = ltr[i] * nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            rtl[(rtl.length - 1) - (i + 1)] = rtl[(rtl.length - 1) - (i)] * nums[nums.length - 1 - i];
        }

        int[] answer = new int[nums.length];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = ltr[i] * rtl[i + 2];
        }

        return answer;
    }
}  
