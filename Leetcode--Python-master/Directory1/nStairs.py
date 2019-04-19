'''
Problem:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Logic:
Recurrence relation..
ans: num_of_ways T(n)= T(n-1) + T(n-2).
answer will be n+1 th fibonacci number.

if n=2, 3rd fibonacci number is the ans.
'''


class Solution:
    def fibonacci(self, n):
        """
        :param n: int
        :return: int
        """
        a, b = 0, 1
        for i in range(n):
            a, b = a + b, a
        return a

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_of_ways=self.fibonacci(n + 1)
        return num_of_ways


if __name__=="__main__":
    obj=Solution()
    res=obj.climbStairs(35)
    print(res)