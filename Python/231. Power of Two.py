# Runtime: 22ms | Beats 99.58% of submissions
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p = 1
        while p <= n:
            if p == n: return True
            p *= 2
        return False
