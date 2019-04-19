'''
Problem: J is string of distinct jewels and S is string of stones.
Question - how many stones are jewels ?
Ex: J='ab' S="aaAbbb" output: 5.
Ex: J='za' S='aAbfdzzaa' output: 5.
'''


class Solution:
    def numofJewlsinStones(self,J ,S):
        """

        :param J: string
        :param S: string
        :return: int

        Logic: for each character in J, count the occurrence of it in S.
        """
        total_jewels = 0
        for j in J:
            total_jewels += S.count(j)
        return total_jewels


if __name__=="__main__":
    obj = Solution()
    J = "ab"
    S = "aaAbbb"
    result = obj.numofJewlsinStones(J, S)
    print(result)