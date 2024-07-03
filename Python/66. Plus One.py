# Runtime: 23ms | Beats 99.45% of submissions
def plusOne(self, digits: List[int]) -> List[int]:
      s = ''
      for d in digits:
          s += str(d)
      out = str(int(s) + 1)

      return [int(n) for n in out]
