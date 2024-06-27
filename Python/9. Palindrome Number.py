# Runtime: 29ms : Beats 90.73% of submissions
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sx = str(x)
        return sx == sx[::-1]
