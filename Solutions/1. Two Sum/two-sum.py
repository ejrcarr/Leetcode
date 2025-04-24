class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i, value in enumerate(nums):
            difference = target - value
            if difference in previous:
                return [previous[difference], i]
            previous[value] = i
