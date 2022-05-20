
# 448. Find All Numbers Disappeared in an Array

## Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


### SOLUTION 1 ###

### Runtime: 489 ms, faster than 40.59% of Python3 online submissions for Find All Numbers Disappeared in an Array.
### Memory Usage: 23.7 MB, less than 49.42% of Python3 online submissions for Find All Numbers Disappeared in an Array.


class Solution:
    def findDisappearedNumbers(self, nums):
        answer = []
        hashmap = {}
        for i in nums:
            hashmap[i] = i
        for i in range(1, len(nums) + 1):
            if i not in hashmap:
                answer.append(i)
        return answer
