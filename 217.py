
# 217. Contains Duplicate

## Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Runtime: 783 ms, faster than 12.28% of Python3 online submissions for Contains Duplicate.
### Memory Usage: 26.1 MB, less than 5.22% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums):
        a = len(nums)
        b = len(set(nums))
        return a > b

### Runtime: 773 ms, faster than 13.27% of Python3 online submissions for Contains Duplicate.
### Memory Usage: 26.1 MB, less than 30.26% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums): 
        return len(nums) > len(set(nums))
