# Runtime 30ms | Beats 89.76% of submissions
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iter_t = iter(t)
        return all(letter in iter_t for letter in s)
