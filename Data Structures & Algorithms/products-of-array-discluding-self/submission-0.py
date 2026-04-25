class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = self.build_prefix(nums, n)
        suffix = self.build_suffix(nums, n)
        ans = [-1] * n

        for i in range(n):
            ans[i] = prefix[i] * suffix[i+1]

        return ans


    def build_prefix(self, nums, n):
        prefix = [1] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]

        return prefix

    def build_suffix(self, nums, n):
        suffix = [1] * (n+1)

        for i in range(n, 0, -1):
            suffix[i-1] = suffix[i] * nums[i-1]

        return suffix
        