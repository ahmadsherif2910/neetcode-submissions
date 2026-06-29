class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l=len(s)
        print(l)
        for i in range(int(l/2 if l%2==0 else l//2+1)):
            j = l-i-1
            print(i,s[i],j,s[j])
            if s[j] != s[i]:
                return False
        return True
