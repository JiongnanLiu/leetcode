"""
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.



"""



class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        i = 0
        sum = 0
        while N > 0:
            sum = sum + (2 ** i) * (0 if N & 1 == 1 else 1)
            i += 1
            N = N >> 1
        return sum


class Solution2:
    def bitwiseComplement(self, N: int) -> int:
        bi = self.toBinary(N)
        print(bi)
        res = ""
        for s in bi:
            if s == '1':
                res = res + '0'
            elif s == '0':
                res = res + '1'
        print(res)
        res = self.toDecimal(res)
        
        return res
    
    
    def toBinary(self, N: int)->str:
        if N == 0:
            return '0'
        res = ""
        while (N > 0):
            rem = N % 2
            res = str(rem) + res
            N = N // 2
        if N == 1:
            res = '1' + res
        return res
    
    def toDecimal(self, N: str)->int:
        res = 0
        l = len(N) - 1
        e = 0
        while (l >= 0):
            res = res + int(N[l]) * 2 ** e
            e += 1
            l -= 1
        return res