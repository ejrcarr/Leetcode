class Solution:
def countSubarrays(self, nums: List[int]) -> int:
    l, r = 0, 2
    count = 0
    while r < len(nums):
        if (nums[l] + nums[r]) * 2 == nums[l + 1]:
            count += 1
        l += 1; r += 1
    return count
