'''
Given two two strings, in binary return there sum in decimal.
Ex: a="101" b="100" output: 1001
Ex: a="1111" b="101" output: 10100
'''


class Solution:
    def bin_to_dec(self, n_bin):
        """

        :param n_bin: binary string
        :return: int decimal equivalent

        logic: say n_bin = 100, 1*2^2 + 0*2^1+ 0*2^0.
        Initially it is reversed bcoz we start conversion from right.
        """
        n_bin_rev = n_bin[::-1]
        power_of_2 = 0
        decimal = 0
        for i in n_bin_rev:
            decimal += int(i)*(2**power_of_2)
            power_of_2 += 1
        return decimal


    def dec_to_bin(self, n_dec):
        """

        :param n_dec: string
        :return: string binary equivalent of decimal.

        Logic: repeatedly divide the num by 2 and keep adding remainders.
        at last reverse the remainders bcoz it is read from downside first.
        """
        binary = ""
        while n_dec != 0:
            remainder = str(n_dec % 2)
            binary = binary + remainder
            n_dec = n_dec // 2
        return binary[::-1]

    def addBinary(self,a,b):
        """

        :param a: binary string
        :param b: binary string
        :return:  binary string

        Logic: convert a and b to decimal. add it. convert result back to binary and return it.
        """

        a_dec = self.bin_to_dec(a)
        b_dec = self.bin_to_dec(b)
        dec_sum = a_dec + b_dec
        #print(dec_sum)
        result = self.dec_to_bin(dec_sum)
        #print(result)
        return result

if __name__=="__main__":
    obj=Solution()
    a="101"
    b="1111"
    obj.addBinary(a,b)