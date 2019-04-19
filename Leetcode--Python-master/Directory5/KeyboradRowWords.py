"""
Identify words whose letters should lie in the same row in qwerty keyboard.

Example: wow, alaska, dad

"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top_row = list("qwertyuiop")
        middle_row = list("asdfghjkl")
        bottom_row = list("zxcvbnm")

        final_list = []
        for i in words:
            i = i.lower()
            i = list(i)
            # check for top row
            if not set(i).difference(set(top_row)):
                temp = ''.join(i)
                final_list.append(temp)
            elif not set(i).difference(set(middle_row)):
                temp = ''.join(i)
                final_list.append(temp)
            elif not set(i).difference(set(bottom_row)):
                temp = ''.join(i)
                final_list.append(temp)

        print(final_list)


if __name__ == "__main__":
    ob = Solution()
    lst = ["Hello","Alaska","Dad","Peace","wow"]
    ob.findWords(lst)