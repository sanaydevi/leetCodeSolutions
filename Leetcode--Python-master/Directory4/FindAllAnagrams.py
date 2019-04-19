"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_sorted = ''.join(sorted(p))
        p_len = len(p_sorted)
        start_index_list = []
        s_len = len(s)

        for i in range(0, s_len, 1):
            temp = ''.join(sorted(s[i:i + p_len]))
            if temp == p_sorted:
                start_index_list.append(i)

        print(start_index_list)


if __name__ == "__main__":
    s = "abab"
    p = "ab"
    ob = Solution()
    ob.findAnagrams(s, p)
