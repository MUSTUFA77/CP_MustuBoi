class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for i in s:
            if i.isalnum():
                new+=i
        if new[-1::-1]==new:
            return True
        return False

        