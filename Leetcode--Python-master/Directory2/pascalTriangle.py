'''
Problem:
To generate pascal's triangle.

Logic:
from the numRows, take the previous list say [1,2,1].
To populate current_list = add first element, 1+2,2+1, last element.
i.e iterate through the previous list and add the elements, put it in the current_list.
'''


class Solution:

    def __init__(self):
        self.rows = []

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        self.rows.append([1])
        self.rows.append([1, 1])

        if numRows == 1:
            return self.rows[0:1]

        elif numRows == 2:
            return self.rows

        while numRows != len(self.rows):                    # in the end rows should have 'numRows' elements.
            current_row = []
            previous_row = self.rows[-1]                   # from the previous list populate the current list.
            current_row.append(previous_row[0])              # First element is same as previouslist.

            for i in range(0, len(previous_row) - 1):         # iterate through the previous list.
                element = previous_row[i] + previous_row[i + 1]
                current_row.append(element)
            current_row.append(previous_row[-1])        # after filling up, last element is same as previous list.
            self.rows.append(current_row)

        print(self.rows)
        return self.rows


if __name__ == "__main__":
    obj = Solution()
    obj.generate(5)
