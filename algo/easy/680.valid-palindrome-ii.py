class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while (l <= r):
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return self.checkPalindrome(s,l+1,r) or self.checkPalindrome(s,l,r-1)
        return True
    
    def checkPalindrome(self,s,start,end):
        while (start < end):
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
                
        
            