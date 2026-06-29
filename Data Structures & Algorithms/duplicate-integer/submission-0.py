class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = []
        for i, num in enumerate(nums):
            if num in prev:
                return True
            else:
                prev.append(num)
        return False