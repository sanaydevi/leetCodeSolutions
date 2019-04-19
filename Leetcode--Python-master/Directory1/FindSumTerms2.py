"""
Problem: Given a list of numbers and target, find two numbers in the list that add up to the target.

Logic:
Use dictionary. Ex: lst=[2,1,3,6,7,8] target is 5. (ans is 2,3.
store difference as key and number as value. like 3:2 4:1 when you encounter 3, d[3] you know it is already there.
"""


class SumTerm:

    def __init__(self):
        self.dict = {}           # used to store all the elements in above described fashion
        self.result = []         # will have the final result elements.

    def findsumterms (self, n, s):
        '''
        :param n: list
        :param s: int value
        :return: int value
        '''
        for i in n:
            if i not in self.dict:
                self.dict[s - i]=i
            else:
                self.result.append((i, self.dict[i]))
        return self.result


if __name__=="__main__":
    ob= SumTerm()
    twonumbers = ob.findsumterms([0, 9, 2, 1, 8], 10)
    print("Sum terms are {}".format(twonumbers))