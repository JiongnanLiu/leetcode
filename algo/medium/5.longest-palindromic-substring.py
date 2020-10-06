"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end - start:
                
                start = i - (max_len-1)//2
                end = i + max_len//2
            
        res = s[start:end+1]
        return res
    
    
    
    def expandAroundCenter(self, s:str, left:int, right:int)->str:
        l = left
        r = right
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return r - l - 1
    