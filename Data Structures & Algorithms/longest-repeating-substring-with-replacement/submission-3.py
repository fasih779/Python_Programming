class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ha = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            ha[s[r]] += 1

            maxfreq = max(ha.values())

            while (r - l + 1) - maxfreq > k:
                ha[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res