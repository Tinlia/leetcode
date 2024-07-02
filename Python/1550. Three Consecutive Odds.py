# Runtime 49ms | Beats 68.73% submissions
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        for i in range(len(arr)-2):
            # If first check is odd
            if arr[i] % 2 == 1:
                # If second check is odd
                if arr[i+1] % 2 == 1:
                    # If final check is odd
                    if arr[i+2] % 2 == 1:
                        return True
                    else: i += 3
                else:i += 2
            else: i += 1
        return False
