# Runtime 19ms | Beats 94.94% of solutions
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        result = 0
        prev = 0
        for i in s:
            if prev < roman_dict[i]:
                result -= prev * 2
            result += roman_dict[i]
            prev = roman_dict[i]
        return result
