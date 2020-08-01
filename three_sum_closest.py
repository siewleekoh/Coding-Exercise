
###################################################################################################################
'''
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Eg.
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
###################################################################################################################

'''
Two Pointer solution:
    Sort the numbers from lowest to highest. For each number i in the list, fixed
    i and sum the i, i+1 and the last number, l. If the sum < target, sum i, i+2 and
    l. If sum > target, sum i, i+1 and l-1. Repeat until a closest three sum is found.
Time complexities: O(n^2), two loops.

'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                summ = nums[i] + nums[lo] + nums[hi]
                if abs(target - summ) < abs(diff):
                    diff = target - summ
                if summ < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break

        return target - diff
