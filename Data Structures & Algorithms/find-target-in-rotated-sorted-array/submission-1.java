class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (right >= left) {
            int mid = left + (right - left) / 2;

            if (nums[left] == target) {
                return left;
            } else if (nums[mid] == target) {
                return mid;
            } else if (nums[right] == target) {
                return right;
            }

            boolean isLeftSideIncreasing = nums[left] < nums[mid];
            boolean containsLeft = Math.min(nums[left], nums[mid]) <= target && target <= Math.max(nums[left], nums[mid]);
            boolean containsRight = Math.min(nums[right], nums[mid]) <= target && target <= Math.max(nums[right], nums[mid]);

            System.out.println(isLeftSideIncreasing + " " + containsLeft + " " + containsRight + " " + left + " " + mid + " " + right);

            if (isLeftSideIncreasing) {
                if (containsLeft) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (containsRight) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}
