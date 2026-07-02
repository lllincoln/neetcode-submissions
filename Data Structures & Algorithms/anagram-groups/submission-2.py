class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for s in strs:
            sorted_str = "".join(sorted(s))
            
            if sorted_str in table:
                table[sorted_str].append(s)
            else:
                table[sorted_str] = [s]
        
        return list(table.values())