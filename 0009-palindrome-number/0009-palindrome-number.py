class Solution:
    def isPalindrome(self, x: int):
        return True if str(x) == str(x)[::-1] else False