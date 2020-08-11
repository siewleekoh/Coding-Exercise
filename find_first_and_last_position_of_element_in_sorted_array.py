###############################################################################
'''

Given an array of integers nums sorted in ascending order, find the starting and
 ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].


Example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9

'''
################################################################################


'''
Brute force (for loop) solution:
Time complexities:  O(n)
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #print([nums.index(x) for x in nums if x == target ])

        index = []
        for i in range(len(nums)):
            if nums[i] == target:
                index.append(i)
        if len(index) == 0:
            index = [-1,-1]
        if len(index) == 1:
            index.append(index[0])
        if len(index) > 2:
            index = list(index[i] for i in [0, len(index)-1] )

        return index

'''
Linear Scan solution:
Time complexities:  O(n)
'''
class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]





'''
Binary Search solution:
Time complexities:  O(log10 n)
'''

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
