################################################################################
'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.


Examples:
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0

'''
################################################################################


'''
Brute force (for loop) solution:
Time complexities: O(n^2), two loops.
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target in nums:
                return nums.index(target)
            elif target > max(nums):
                return len(nums)
            elif target < min(nums):
                return 0
            elif target > nums[i] and target < nums[i+1]:
                return i + 1



'''
Time complexities: O(n), onw loop.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
