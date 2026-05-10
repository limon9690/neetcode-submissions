class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        fixed_map = {}
        curr_map = {}
        j = 0

        for i in range(len(s1)):
            fixed_map[s1[i]] = fixed_map.get(s1[i], 0) + 1


        for i in range(len(s1)):
            curr_map[s2[i]] = curr_map.get(s2[i], 0) + 1


        if curr_map == fixed_map:
            return True


        for i in range(len(s1), len(s2)):
            curr_map[s2[i]] = curr_map.get(s2[i], 0) + 1
            curr_map[s2[j]] = curr_map.get(s2[j], 0) - 1

            if curr_map[s2[j]] == 0:
                del curr_map[s2[j]]

            if curr_map == fixed_map:
                return True

            j += 1

        return False