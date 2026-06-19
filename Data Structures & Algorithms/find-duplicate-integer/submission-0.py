class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        while i < n:
            corr_idx = nums[i] - 1
            if nums[i] != nums[corr_idx]:
                nums[i], nums[corr_idx] = nums[corr_idx], nums[i]
            else:
                i += 1

        
        ans = -1
        i = 0
        while i < n:
            if nums[i] != i+1:
                ans = nums[i]

            i += 1

        return ans