class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];

        for (int i = 0; i < result.length; i++) {
            boolean found = false;

            for (int j = i+1; j < result.length; j++) {
                if (temperatures[i] < temperatures[j]) {
                    found = true;
                    result[i] = j-i;
                    break;        
                }
            }

            if (!found) {
                result[i] = 0;
            }
        }

        return result;
    }
}
