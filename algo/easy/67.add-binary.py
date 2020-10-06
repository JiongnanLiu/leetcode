"""
67. Add Binary
Easy

2148

296

Add to List

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        ia = len(a)-1
        ib = len(b)-1
        carry = 0 
        while  (ia >= 0 or ib >= 0):
            if ia >= 0:
                ta = ord(a[ia]) - ord('0')
            else:
                ta = 0
            if ib >= 0:
                tb = ord(b[ib]) - ord('0')
            else:
                tb = 0
            
            value = tb + ta + carry
            if value == 3:
                carry = 1
                res.append(1)
            elif value == 2:
                carry = 1
                res.append(0)
            elif value == 1:
                carry = 0
                res.append(1)
            else:
                carry = 0
                res.append(0)
            ia -= 1
            ib -= 1
        if carry == 1:
            res.append(1)
            
        return ''.join(str(x) for x in res[::-1])