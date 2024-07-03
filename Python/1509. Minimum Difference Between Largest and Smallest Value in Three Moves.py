# Runtime: 266ms | Beats 84.62% of solutions
class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4: return 0  # If 4 or fewer, can make all equal
        nums.sort()
        # Compare differences after removing three from the start, end, or mix
        return min(
            nums[-1] - nums[3],  # Remove three smallest
            nums[-2] - nums[2],  # Remove two smallest, one largest
            nums[-3] - nums[1],  # Remove one smallest, two largest
            nums[-4] - nums[0]   # Remove three largest
        )
        
