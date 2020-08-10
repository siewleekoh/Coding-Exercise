###############################################################################
'''

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''
################################################################################


'''
Brute force (for loop) solution:
Time complexities:  O(n^2)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        alistOflist = []
        for i, word in enumerate(strs):
            alist = []
            alist.append(strs[i])

            j = i + 1
            while j < len(strs):
                if set(word) == set(strs[j]):
                    alist.append(strs[j])
                    strs.remove(strs[j])
                j += 1
            alistOflist.append(alist)

        return alistOflist


'''
Categorize by Sorted String solution:
Time complexities:   O(NK \log K)O(NKlogK), where NN is the length of strs,
and KK is the maximum length of a string in strs.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
