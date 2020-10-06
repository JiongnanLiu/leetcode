"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dups = set()
        seen = {}
        for i ,v1 in enumerate(nums):
            if v1 not in dups:
                dups.add(v1)
                for j, v2 in enumerate(nums[i+1:]):
                    complement = -v1 - v2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((v1, v2, complement))))
                    seen[v2] = i
        return res
        
