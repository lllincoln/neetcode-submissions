class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_nums = sorted(nums)
        current_seq_len = 1
        max_seq_len = 1
        
        for idx in range(1, len(sorted_nums)):
            num = sorted_nums[idx]
            previous_num = sorted_nums[idx - 1]
            diff = num - previous_num

            if diff == 0:
                continue
            elif diff == 1:
                current_seq_len += 1
            else:
                current_seq_len = 1
            
            max_seq_len = max(current_seq_len, max_seq_len)

        return max_seq_len