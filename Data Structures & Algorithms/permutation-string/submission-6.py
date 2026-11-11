from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ha1=Counter(s1)
        l=0
        for r in range(len(s1)-1,len(s2)):
            ha2=Counter(s2[l:r+1])
            if ha1==ha2:
                return True
            l+=1
        return False        
      