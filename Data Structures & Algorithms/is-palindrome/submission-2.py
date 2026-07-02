class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""

        for c in s:
            c = c.lower()

            if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
                filtered += c

        s = filtered

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        
        return True