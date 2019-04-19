"""
Given p and s check if both pattern matches or not.

Logic:
Make a key , value pair in dictionary. Check if all the pattern validates. If not then it is an
error.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict_pattern = {}
        for p, s in zip(list(pattern), str.split(" ")):
            if p not in dict_pattern:
                dict_pattern[p] = s
            else:
                if dict_pattern[p] != s:
                    return False

        pattern_no_dup = list(set(list(pattern)))
        for i in range(len(pattern_no_dup)):
            if dict_pattern[pattern_no_dup[i]] == dict_pattern[pattern_no_dup[i + 1]]:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()
    p = "abba"
    s = "dog dog dog dog"
    res = obj.wordPattern(p, s)
    print(res)
