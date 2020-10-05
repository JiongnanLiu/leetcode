class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < -2 ** 31:
            return 0
        if x == 0:
            return x
        neg = False
        if x < 0:
            x = -x
            neg = True
        x = str(x)
        while (x[-1] == '0'):
            x = x[:-1]
        x = x[::-1]
        res = 0
        if neg:
            res = -int(x)
        else:
            res = int(x)
        if res > 2**31 - 1 or res < -2 ** 31:
            return 0
        else:
            return res