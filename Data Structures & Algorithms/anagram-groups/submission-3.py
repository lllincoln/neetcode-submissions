class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for s in strs:
            identity = [0] * 26

            for c in s:
                idx = ord(c) - ord('a')
                identity[idx] += 1
            
            identity = str(identity)

            if identity in table:
                table[identity].append(s)
            else:
                table[identity] = [s]
        
        return list(table.values())