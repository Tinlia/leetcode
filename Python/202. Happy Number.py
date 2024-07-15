class Solution:
    def isHappy(self, n: int) -> bool:
        sum = n
        loop = []
        while sum != 1:
            sum = 0
            for num in str(n):
                sum += int(num)**2
            if sum in loop: return False
            loop.append(sum)
            n = sum
        return True
