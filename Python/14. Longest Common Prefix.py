class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # If strings is empty, return empty string
        if not strs:
            return ""

        # If there is only one string, return the string
        if len(strs) == 1:
            return strs[0]
        
        # Recursively check if the first min_len letters of the first word exist in all words
        def check(min_len):
            if min_len == 0:
                return ""
            prefix = strs[0][:min_len]
            for word in strs[1:]:
                if prefix != word[:min_len]:
                    # If the prefix is not the same, check the next min_len-1 letters
                    return check(min_len-1)
            # If the prefix is found in every word, return it
            return prefix

        return check(min(len(word) for word in strs))
