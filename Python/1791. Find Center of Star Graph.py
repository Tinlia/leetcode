# Runtime: 575ms | Beats 98.08% of submissions
# Time complexity: O(1)
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges[0][0] in edges[1]:
            return edges[0][0]
        elif edges[0][1] in edges[1]:
            return edges[0][1]

# If there exists a common point in every pairing of edges, it must exist in the first two edge pairs. 
# Additionally, since the graph is a star, there should only be one point that is visited more than once. 
# Since that point must exist in the first two pairs, simply finding the node that occurs in both of the first two pairs will return the center.
