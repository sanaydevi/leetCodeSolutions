"""
Problem:
This is a implementation of MaxSubArray problem in o(n) time complexity.
Kadane's algorithm.

Logic:
At each point decide to choose i or currenct_sum+i.

"""


class MaxSubArray:
    def __init__(self):
        self.currentMax = 0
        self.maxSoFar = 0
        self.hasPositive = False

    def maxsubarray(self, n):
        '''

        :param n: list
        :return:  int
        '''
        for j in n:                   # determining if it has at least 1 positive num
            if j > 0:
                self.hasPositive=True

        if self.hasPositive:          # follow the kadane's algorithm
            for i in n:
                self.currentMax += i

                if self.currentMax < 0:
                    self.currentMax = 0

                if self.maxSoFar<self.currentMax:
                    self.maxSoFar=self.currentMax

        else:
            self.maxSoFar = max(n)      # no positive num. return the max of negative numbers.

        return self.maxSoFar


if __name__ == "__main__":
    l = [-2,-3,-4,5,6,-12]
    ob = MaxSubArray()
    maxSum = ob.maxsubarray(l)
    print("Max sub sum is {}".format(maxSum))





