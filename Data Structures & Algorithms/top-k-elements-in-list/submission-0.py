class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}

        for n in nums:
            if n in occur:
                occur[n] += 1
            else:
                occur[n] = 1
        
        sorted_by_occur = sorted(occur.items(), key=lambda item: item[1], reverse=True)

        return [sorted_by_occur[i][0] for i in range(k)] 