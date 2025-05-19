class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_that_complete = {}
        for i, num in enumerate(nums):
            missing_num = target - num
            if num in nums_that_complete:
                return [nums_that_complete[num], i]
            else:
                nums_that_complete[missing_num] = i