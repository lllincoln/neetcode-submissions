class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in nums:
            streak = 0
            current = num

            while current in num_set:
                current += 1
                streak += 1
            
            result = max(result, streak)

        return result