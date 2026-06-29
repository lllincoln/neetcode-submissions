class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = []

        for i, n in enumerate(nums):
            req = target - n
            
            try:
                j = nums.index(req, i+1)
                if j > -1:
                    return [i, j]
            except:
                pass
