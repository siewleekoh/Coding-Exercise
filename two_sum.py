###################################################################################################################
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
###################################################################################################################


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

'''
Brute force (for loop) solution:
Time complexities: O(n^2), two loops.
'''

#         ans = []
#         for i, num in enumerate(nums):
#             print('num:', num, ', at index', i)
#             complement = target - num
#             if complement in nums:
#                 index1 = i
#                 index2 = nums.index(complement)
#                 if index1 == index2:
#                     continue
#                 else:
#                     ans.append(index1)
#                     ans.append(index2)
#                     break
#     return ans

'''
One pass hash table solution: implement hash table in python using dictionary.
Time complexities: O(n), one loop.
'''
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
