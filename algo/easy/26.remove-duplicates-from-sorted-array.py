class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        while (ptr2 < len(nums)):
            while(ptr2 < len(nums) and nums[ptr2] == nums[ptr1]):
                #increment ptr2 by 1 until it pointer to a non-duplicate one.
                ptr2 += 1
            
            #now ptr2 points to an item not equal to item pointed to by ptr1
            if (ptr2 < len(nums)):
                #swap the item next to ptr1
                nums[ptr1+1], nums[ptr2] = nums[ptr2], nums[ptr1+1]
                ptr2 += 1
                ptr1 += 1
        return ptr1+1 #plus 1 because it requires to output the length of the array.