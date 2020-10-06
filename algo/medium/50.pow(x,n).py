class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n % 2 == 0:
            return self.myPow(self.myPow(x, 2), n>>1)
        elif n % 2 == 1:
            return x * self.myPow(self.myPow(x, 2), (n-1)>>1)


class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:return 1
        sign=n>0
        n=abs(n)
        pw=x
        ans=1
        while n:
            if n&1==1:
                ans*=pw
            pw*=pw
            n=n>>1
            print(n)
        if sign==0:
            ans=1/ans
        return ans