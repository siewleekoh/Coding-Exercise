###################################################################################################################
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
###################################################################################################################

'''
Two Pointer solution:
    Assign the area between the left most point, l and the right most point, r
    as the maximum area. If the r point is higher than that of the l point,
    then move the left point to l+1 and find this area. Else if r point is
    lower than l point, move the right point to r+1 and find this area. Repeat
    as long as the r index is bigger than r index.
Time complexities: O(n), while loop.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:

#         maxarea = 0
#         l = 0
#         r = len(height) -1

#         while r > l:
#             maxarea = max(maxarea, min(height[r], height[l]) * (r-l))
#             if height[l] < height[r]:
#                 l =+ 1
#             else:
#                 r =- 1

#         return maxarea

 #### above code exceed time limit ####


        maxarea = 0
        l = 0
        r = len(height) - 1

        for cnt in range(len(height)):
            width = abs(l - r)

            if height[l] < height[r]:
                res = width * height[l]
                l += 1
            else:
                res = width * height[r]
                r -= 1

            if res > maxarea:
                maxarea = res

        return maxarea
