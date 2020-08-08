###################################################################################################################
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.




'''
###################################################################################################################


'''
Sliding Window solution:
Time complexities:  O(2n) = O(n).
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        adict = {}
        for i in range(len(s)):
            astr = s[i]
            for j in range(len(s) - i -1):
                z = i + j
                if s[z+1] in astr:
                    break
                else:
                    astr += s[z+1]

            adict[astr] = len(astr)

            ans = max(adict.values())

        return  ans
