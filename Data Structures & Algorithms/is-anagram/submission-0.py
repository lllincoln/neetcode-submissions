class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_table_s = {}
        hash_table_t = {}

        for char in s:
            if char in hash_table_s:
                hash_table_s[char] += 1
            else:
                hash_table_s[char] = 1
        
        
        for char in t:
            if char in hash_table_t:
                hash_table_t[char] += 1
            else:
                hash_table_t[char] = 1    

        return hash_table_s == hash_table_t