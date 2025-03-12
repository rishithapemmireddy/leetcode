class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.replace(" ","").lower()
        for letter in s:
            if not letter.isalnum():
                s=s.replace(letter,"")
            
        dup=s[::-1]
        if s==dup:
            return True
        else:
            return False
        