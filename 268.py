
# 268. Missing Number

## Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


### SOLUTION 1 ###

### Runtime: 195 ms, faster than 47.00% of Python3 online submissions for Missing Number.
### Memory Usage: 15.5 MB, less than 14.60% of Python3 online submissions for Missing Number.

class Solution:
    def containsDuplicate(self, nums):
        hashmap = {}
        for i in nums:
            hashmap[i] = i
        for i in range(len(nums) + 1):
            if i not in hashmap:
                return i
