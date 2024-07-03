# Runtime: 37ms | Beats 91% of submissions
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[\W_]+', '', s).lower()
        return s == s[::-1]
