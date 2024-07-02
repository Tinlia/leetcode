# Runtime: 26ms | Beats 96.3% of submissions
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
