class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in h:
                h[num] = i
            else:
                return [h[complement], i]