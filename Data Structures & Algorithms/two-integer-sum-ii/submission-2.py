class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1

        while True:
            left = numbers[left_idx]
            right = numbers[right_idx]

            if left > right:
                break

            s = left + right

            if s == target:
                return [left_idx+1, right_idx+1]
            elif s > target:
                right_idx -= 1
            else:
                left_idx += 1
        
        return []
