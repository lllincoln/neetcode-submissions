class Solution {
    public static  int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (right != left) {
            int mid = left + (right - left) / 2;

            if (left == mid && nums[left] > nums[right]) {
                return nums[right];
            }
            
            if (nums[right] > nums[left]) {
                return nums[left];
            }

            if (nums[mid] < nums[right] && nums[right] < nums[left]) {
                right = mid;
            } else if (nums[right] < nums[left] && nums[left] < nums[mid]) {
                left = mid;
            }
        }

        return nums[left];
    }
}
