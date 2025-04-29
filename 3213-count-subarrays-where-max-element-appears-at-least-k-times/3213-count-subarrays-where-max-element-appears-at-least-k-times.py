class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        left = 0
        result = 0

        for right, num in enumerate(nums):
            if num == max_num:
                count += 1

            while count == k:
                if nums[left] == max_num:
                    count -= 1
                left += 1
            result += left
        return result