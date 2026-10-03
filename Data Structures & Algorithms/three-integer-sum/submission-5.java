class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        // -1  0   1   2  -1  -4
        // -4  -1  -1  0   1   2 
        //      i      L   R
        //          i  L   R        

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i+1;
            int right = nums.length-1;

            if (i > 0 && nums[i-1] == nums[i]) {
                continue;
            }

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum < 0) {
                    // need to increase
                    left++;
                } else if (sum > 0) {
                    // need to decrease
                    right--;
                } else {
                    // sum == 0
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[left]);
                    temp.add(nums[right]);
                    result.add(temp);

                    int skip = nums[left];

                    while (left < right && skip == nums[left]) {
                        left++;
                    }
                }
            }
        }

        return result;
    }
}
