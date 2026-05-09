class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        mp = {}
        max_char = 0
        ans = 0
        j = 0

        for i in range(n):
            mp[s[i]] = mp.get(s[i], 0) + 1
            max_char = max(max_char, mp[s[i]])

            while ((i-j+1) - max_char) > k:
                mp[s[j]] = mp.get(s[j], 0) - 1
                j += 1

            ans = max(ans, (i-j+1))


        return ans