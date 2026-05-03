class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = {}

        for i in range(n):
            count[nums[i]] = i


        for i in range(n):
            curr = 1
            key = nums[i]

            if (key - 1) in count:
                continue

            while (key + 1) in count:
                curr += 1
                key = key + 1

            ans = max(ans, curr)


        return ans