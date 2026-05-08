class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        count = {}
        ans = 0

        for i in range(n):
            count[s[i]] = count.get(s[i], 0) + 1

            while count[s[i]] > 1:
                count[s[j]] = count.get(s[j], 0) - 1

                if count[s[j]] == 0:
                    del count[s[j]]

                j += 1

            ans = max(ans, (i-j+1))


        return ans