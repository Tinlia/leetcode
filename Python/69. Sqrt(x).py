# Runtime: 31ms | Beats 93.13% of submissions
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        k=math.sqrt(x)
        return math.floor(k)
