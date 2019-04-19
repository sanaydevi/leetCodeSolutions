"""
Problem:
This is the implementation of Factorial of a number.
Used reduce - which is a built in type of python.


Logic: 
reduce takes list as a and returns a single value. 
For Ex: a=[1,2,3,4] , list a is passed to reduce.
lambda takes two values at a time. Next iteration result of the previous operation and one more value from the list.  
"""
from functools import  reduce

class Factorial:

    def __init__(self,num):
        self.num=num

    def computeFactorial(self):
        '''
        :return: int value
        '''
        numList= range(1,self.num+1)           #generate a list including num.
        return reduce(lambda a,b: a*b,numList)


if __name__=="__main__":
    ob= Factorial(6)
    result=ob.computeFactorial()
    print("Factorial of 6 is {}".format(result))