'''
Problem:  check for panlindrome sentence considering only alpha numeric characters.

Logic: first extract all alphanumeric characters and check for palindrome.
'''
import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        patterns = [r'\w+']

        for p in patterns:
            match = re.findall(p, s)

        filtered_string = "".join(match)
        filtered_string = filtered_string.lower()

        if filtered_string == filtered_string[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Solution()
    s = "A man, plan, a canal: Panama"
    print(obj.isPalindrome(s))
