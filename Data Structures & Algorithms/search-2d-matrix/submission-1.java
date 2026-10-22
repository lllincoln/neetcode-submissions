class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int left = 0;
        int right = m*n - 1;

        while (right >= left) {
            int mid = left + (right - left) / 2;
            int row = mid / n;
            int col = mid % n;

            System.out.println("mid: " + mid + ", row: " + row + ", col: " + col);

            int num = matrix[row][col];

            if (num > target) {
                right = mid - 1;
            } else if (num < target) {
                left = mid + 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
