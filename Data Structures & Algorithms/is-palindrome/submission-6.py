class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ''
        s = s.replace(" ", "")
        s = s.lower()

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                rev += s[i]

        s = ''.join(i for i in s if i.isalnum())

        if rev == s:
            return True
        else:
            return False