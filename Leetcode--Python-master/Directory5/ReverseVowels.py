'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

Logic:
Find all the list of vowels in the string using regex.
Iterate the string and for the fist occurrence of the vowel in the string, substitute the last vowel from the list.
complete the full string.

'''

import re


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        pattern = re.compile(r'[aeiouAEIOU]')
        match = pattern.findall(s)

        vowellist = [m for m in match]
        return re.sub('(?i)[aeiou]', lambda m: vowellist.pop(), s)


if __name__ == "__main__":
    obj = Solution()
    print(obj.reverseVowels("leetcode"))
