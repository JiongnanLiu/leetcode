class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        value = 0
        while (p1 >= 0 or p2 >= 0):
            if p1 >= 0:
                v1 = ord(num1[p1]) - ord('0')
            else:
                v1 = 0
            if p2 >= 0:
                v2 = ord(num2[p2]) - ord('0')
            else:
                v2 = 0
                
            temp = (v1 + v2 + carry)
            value = temp % 10
            carry = temp // 10
            res.append(value)
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(carry)
        
        
        return ''.join(str(x) for x in res[::-1])
            