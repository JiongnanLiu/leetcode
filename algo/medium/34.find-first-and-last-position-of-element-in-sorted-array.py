"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.bSearch(nums, target, "left"), self.bSearch(nums, target, "right")]
            
    def bSearch(self, nums, target, mode):
        l = 0
        r = len(nums) - 1
        res = -1
        while (l <= r):
            mid = int((r + l)/2)
            if (nums[mid] > target):
                r = mid-1
            elif (nums[mid] < target):
                l = mid+1
            else:
                res = mid
                if(mode == "left"):
                    r = mid - 1
                elif(mode == "right"):
                    l = mid + 1
        return res

class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
        l = 0
        r = len(nums) - 1
        ans = []
        while (l < r):
            while (r >= 0 and nums[r] > target):
                r -= 1
            while (l < len(nums) -1 and nums[l] < target):
                l += 1
            if (nums[l] == target):
                ans.append(l)
            if (nums[r] == target):
                ans.append(r)
            if (len(ans) == 2):
                break
        if not ans:
            return [-1,-1]
        return ans