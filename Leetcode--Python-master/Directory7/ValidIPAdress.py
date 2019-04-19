"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""


class Solution(object):
    '''
    make sure in ipv4 , for each nibble,
    if there is leading zero it false except len ==1
    i.e differentiate between .0. and .018. or .0. and .00. or 0.0.0.0 and 00.0.0.0
    and no -ves.
    '''

    def check_ipv4(self, ip):
        """

        :param ip: list
        :return: string
        """
        # print(ip)
        if ip == ['0'] * 4:
            return "IPv4"

        def helper(x):
            try:
                if ((len(x) - len(x.lstrip('0'))) > 0 and len(x) != 1) or '-' in x:  # imp step.
                    return False

                int_x = int(x)
                if 0 <= int_x <= 255:
                    return True
                else:
                    return False
            except:
                return False

        result = list(map(helper, ip))
        if False in result:
            return 'Neither'
        else:
            return 'IPv4'

    '''
    Make sure there is no -ve in nibble. bcoz leading zeros are allowed. 
    '''

    def check_ipv6(self, ip):
        """

        :param ip: list
        :return: string
        """

        def helper(x):
            try:
                if '-' in x:
                    return False
                if len(x) <= 4:
                    if int == type(int(x, 16)):
                        return True
                    else:
                        return False
                else:
                    return False
            except:
                return False

        result = list(map(helper, ip))
        if False in result:
            return 'Neither'
        else:
            return 'IPv6'

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            break_down_ip = IP.split(".")
            if len(break_down_ip) == 4:
                return self.check_ipv4(break_down_ip)
            else:
                return 'Neither'

        else:
            break_down_ip = IP.split(':')
            if len(break_down_ip) == 8:
                return self.check_ipv6(break_down_ip)
            else:
                return 'Neither'


if __name__ == "__main__":
    ob = Solution()
    res = ob.validIPAddress("0.0.0.0")
    print(res)

"""
Test cases:
"172.16.251.1"
"1e1.4.5.6"
"2001:0db8:85a3:0:0:8A2E:0370:7334"
"2001:0db8:85a3:0:0:8A2E:0370:7334:"
"00.0.0.0"
"1081:db8:85a3:01:-0:8A2E:0370:7334"
"""
