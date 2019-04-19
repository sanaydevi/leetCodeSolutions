'''
Problem: Length of the last word in a given string.
constraints: last word doesn't exist - ret 0.
Ex: s = "this is a sentence", output: 8.
Ex s = "              hi              " , output = 2.
'''


class Solution:
    def lenoflastword(self, s):
        """
        :param s: string
        :return: int

        Logic: first remove the starting and trailing space.
        Then split the string on " ".
        Get the length of last object in the above list.
        """
        s = s.strip()
        if not s:
            return 0
        list_of_words = s.split(" ")
        last_word = list_of_words[ -1 ]
        return len(last_word)


if __name__ == "__main__":
    obj = Solution()
    str = " "
    print("len of last word = {}".format(obj.lenoflastword(str)))
