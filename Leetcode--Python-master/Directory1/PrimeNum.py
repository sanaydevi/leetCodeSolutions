"""
Problem: generate all prime numbers within the given number n.

Logic: eratosthenes algorithm. (ultra fast way)
basically start from 2 and make all multiples of 2 false. 3 is still true so make all multiples of 3 false.
at the end, list has all the prime numbers.
"""
from math import sqrt


class Prime:

    def generatePrimes(self, n):
        '''

       :param n: list
       :return: list
       '''

        primes = [True] * n                              # make a list of True of len n.
        primes[0] = primes[1] = False                    # 0,1 are not prime
        for i in range(2, int(sqrt(n)+1)):               # loop runs only till sqrt of n times.
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])

        prime_list = [i for i,v in enumerate(primes) if v==1]
        return prime_list


if __name__ == "__main__":
    ob = Prime()
    print(ob.generatePrimes(10))
