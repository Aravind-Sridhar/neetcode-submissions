class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''
        for x in s:
            if x.isalnum():
                text+=x.lower()
        l,r = 0, len(text)-1
        while l<r:
            if text[l] != text[r]:
                return False
            l+=1
            r-=1
        return True
        