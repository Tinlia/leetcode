# Runtime: 11ms | Beats 78.68% of submissions
class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        d = {}
        # Get count of all words
        for letter in word:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        count = sorted(d.values(), reverse=True)
      
        # == Edge cases == #
        if len(count) == 1:
            return True
        # If all letters occur the same freq
        if all(x == count[0] for x in count):
            # If the min is 1, return true
            if count[0] == 1:
                return True
            # Else return false
            return False
          
        # If not all letters occur the same freq
        else:
            # If the max-1 makes all the same freq, return true
            if all(x == count[0]-1 for x in count[1:]):
                return True
            # If the min is 1 and removing it makes all the same freq, return true
            if all(x == count[0] for x in count[:-1]) and count[-1] == 1:
                return True
            # else, return false
            return False
