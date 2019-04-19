'''
To generate pascal's triangle and return only rth index row of the pascal triangle.
suppose input is 3, return [1,3,3,1]. Row index starts from 0.

Logic:
Generate the pascal triangle and return the required row.
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

        while numRows+1 != len(self.rows):          # in the end len(rows) should have 'numRows+1' elements bcoz starts from 0.
            current_row = []
            previous_row = self.rows[-1]                  # from the previous list populate the current list.
            current_row.append(previous_row[0])           # First element is same as previouslist.

            for i in range(0, len(previous_row) - 1):      # iterate through the previous list.
                element = previous_row[i] + previous_row[i + 1]
                current_row.append(element)
            current_row.append(previous_row[-1])           # after filling up, last element is same as previous list.
            self.rows.append(current_row)

        #print(self.rows)
        return self.rows[numRows]


if __name__ == "__main__":
    obj = Solution()
    result = obj.generate(3)
    print(result)