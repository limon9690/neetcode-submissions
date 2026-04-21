class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            mp[nums[i]] = i

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in mp and mp.get(comp) != i:
                return [i, mp.get(comp)]

        
        return [-1, -1]