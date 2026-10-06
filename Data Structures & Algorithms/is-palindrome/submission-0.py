class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = ""
        for st in s:
            if st.isalnum():
                an += st.lower()
        
        r = 0
        l = len(an)-1
        
        while r < l:
            if an[r] != an[l]:
                return False
            r += 1
            l -= 1

        return True