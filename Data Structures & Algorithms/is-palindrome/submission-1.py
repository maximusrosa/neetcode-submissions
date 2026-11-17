class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)

        if n == 0:
            return True

        for i in range(n):
            j = (n -1) - i

            if s[i] != s[j]:
                return False
            
            if i >= j:
                return True
        