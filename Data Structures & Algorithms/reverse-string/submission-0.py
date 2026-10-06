class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(size//2):
            print(i, size-1-i)
            s[i], s[size-1-i] = s[size-1-i], s[i]

        return "".join(s)