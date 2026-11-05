class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ha = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ha[s[i]] = ha.get(s[i], 0) + 1
            ha[t[i]] = ha.get(t[i], 0) - 1

        if any(ha.values()):
            return False

        return True