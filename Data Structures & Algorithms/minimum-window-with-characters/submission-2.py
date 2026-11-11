from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        ha1 = Counter(t)
        ha2 = Counter()

        required = len(ha1)
        formed = 0
        res = ""

        for r in range(len(s)):
            ha2[s[r]] += 1

            if s[r] in ha1 and ha2[s[r]] == ha1[s[r]]:
                formed += 1

            while formed == required:
                if not res or r - l + 1 < len(res):
                    res = s[l:r + 1]

                ha2[s[l]] -= 1

                if s[l] in ha1 and ha2[s[l]] < ha1[s[l]]:
                    formed -= 1

                l += 1

        return res