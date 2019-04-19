"""
You can delete at most one character to make string palindrome.
Judge if it is palindrome or not.
"""


class Solution(object):
    def check(self, str):
        if str == str[::-1]:
            return True
        else:
            return False

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        s = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # remove lth element and check.
                temp = s[:]
                temp.pop(l)
                if self.check(temp):
                    return True

                # remove rth element and check.
                temp = s[:]
                temp.pop(r)
                if self.check(temp):
                    return True

                break
            l += 1
            r -= 1
        return False


if __name__ == "__main__":
    ob = Solution()
    s = 'abcbefa'
    res = ob.validPalindrome(s)
    print(res)
