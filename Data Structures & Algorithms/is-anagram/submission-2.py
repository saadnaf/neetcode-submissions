class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = {}
        charT = {}

        if len(s) != len(t):
            return False

        for cs, ct in zip(s, t):
            if cs in charS:
                charS[cs] += 1 
            else:
                charS[cs] = 1

            if ct in charT:
                charT[ct] += 1 
            else:
                charT[ct] = 1
        
        return charS == charT