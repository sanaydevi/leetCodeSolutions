"""
Google interview question.

Generate all combinations of the string - binary string. ? maps to 0 or 1.
10? = 100, 101.
10?? = 1000,10001, 1010, 1011.
10?1 = 1001,1011

Logic :
2d list. keep pushing from original list if number is 0 /1.
if ? , for each item , append 0 and 1 and put it in original list.
"""


class Solution(object):
    def generate_string(self, str):
        final_list = [[]]

        buffer_list = []
        for i in str:
            if i != '?':
                [j.append(i) for j in final_list]   # You don't have assign [] to something always.
            else:
                buffer_list.clear()
                for j in final_list:               # when iterating somelist, do not change it inside the loop.
                    temp = j[:]                    # Put new combination in temp and to buffer list.
                    j.append('0')
                    temp.append('1')
                    buffer_list.append(temp)
                final_list = final_list + buffer_list  # add whatever in buffer_list back to final_list

        print(final_list)


if __name__ == "__main__":
    ob = Solution()
    ob.generate_string("10??")
