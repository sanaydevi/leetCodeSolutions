from math import log


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        trail_num = 2
        while True:
            if log(num, trail_num) == 2.0:
                return True

            elif log(num, trail_num) < 2.0:
                break

            trail_num += 1

        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPerfectSquare(404))
