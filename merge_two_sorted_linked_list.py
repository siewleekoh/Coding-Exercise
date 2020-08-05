################################################################################
'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Examples:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
