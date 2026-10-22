class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (right >= left) {
            int mid = left + (right - left) / 2;
            int num = nums[mid];

            if (num > target) {
                right = mid - 1;
            } else if (num < target) {
                left = mid + 1;
            } else {
                return mid;
            }
        }

        return -1;
    }
}
