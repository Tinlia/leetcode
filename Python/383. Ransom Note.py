# Runtime: 29ms | Beats 91.53% of submissions
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictM = {}
        # Build a "budget" based on count of letters in mag
        for l in set(magazine):
            dictM[l] = magazine.count(l)

        # Compare each unique letter in ransomNote to the budget
        for l in set(ransomNote):
            try:
                if dictM[l] < ransomNote.count(l): return False
            except: # Keyerror if letter not found
                return False
        
        return True
