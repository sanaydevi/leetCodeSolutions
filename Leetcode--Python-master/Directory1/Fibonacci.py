"""
Implementation of Fibonacci numbers.

Logic:
Say you have generated fibonacci numbers: 0,1,1,2,3,5.
To generate next number: now a=3 and b=5.
So what we want is a=5 which is b and b=8 which is a+b. so a, b = b , a+b.
To know more how it works: read tuple unpacking in python.
"""


class Fibonacci:

    def fibo(self, num):
        '''
        :param num: int value
        :return: int value
        '''
        a, b = 0, 1           # initialize with a = 0 and b = 1.
        for i in range(num):
            a, b = b, a+b
        return a              # return a bcoz b would contain a + b which is next fibonacci number.


if __name__ == "__main__":
    obj= Fibonacci()
    print("fibonacci num is {}".format(obj.fibo(6)))
