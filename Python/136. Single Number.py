class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}
        for n in nums:
            try:
                s[n] += 1
            except:
                s[n] = 1
        for n in s:
            if s[n] == 1:
                return n
