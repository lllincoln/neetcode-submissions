class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = Integer.MIN_VALUE;

        while (left < right) {
            int width = right - left;
            int height = Math.min(heights[left], heights[right]);
            int area = width * height;
            maxArea = Math.max(area, maxArea);

            if (heights[left] > heights[right]) {
                right--;
            } else if (heights[left] < heights[right]) {
                left++;
            } else {
                left++;
                right--;
            }
        }

        return maxArea;
    }
}
