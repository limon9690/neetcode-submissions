class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(total, subset, idx):
            if total == target:
                res.append(subset.copy())
                return

            if total > target or idx >= len(candidates):
                return

            subset.append(candidates[idx])
            dfs(total + candidates[idx], subset, idx + 1)

            subset.pop()
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1

            dfs(total, subset, idx + 1)


        dfs(0, [], 0)

        return res          
