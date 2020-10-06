"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hMap = {}
        for i in range(len(strs)):
            count_chr = [0] * 26
            for j in range(len(strs[i])):
                count_chr[ord(strs[i][j])-ord('a')] += 1
        
            k = str(count_chr)
            
            if k not in hMap:
                hMap[k] = []
            hMap[k].append(strs[i])
        
        return hMap.values()

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            ans[k].append(s)
        return ans.values()
        