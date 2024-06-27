# Runtime: 645ms | Beats 83.80% of submissions
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Find and return the number that exists in every pair
        used = []
        def check(n):
            for pair in edges:
                if n not in pair: return False
            return True

        for pair in edges:
            for n in pair:
                if n not in used:
                    if not check(n): used.append(n)
                    else: return n
        return None
