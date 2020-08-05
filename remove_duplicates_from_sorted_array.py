
################################################################################
'''
Given a sorted array nums, remove the duplicates in-place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.


Examples:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being
 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being
modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

'''
################################################################################


'''
two pointers solution:
Since 'set' cannot be used and a new array cannot be used,
we could loop through the array and count the number of unique elements. To keep
track of the unique elements, each new elements encountered in the loop will be
set to as the existing value for the next comparison.

Time complexities: O(n), one loops.
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)<=0):
            return 0
        else:
            i=0
        for j in range(0,len(nums)):
            if(nums[j]!=nums[i]):
                i=i+1
                nums[i]=nums[j]
        return i+1
