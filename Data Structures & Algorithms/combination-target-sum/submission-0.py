class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, subset, total):
            if idx >= len(nums) or total > target:
                return

            if total == target:
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            total += nums[idx]
            dfs(idx, subset, total)

            total -= subset.pop()
            dfs(idx+1, subset, total)
            

        dfs(0, [], 0)

        return res