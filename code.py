class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        i=0
        j=3
        c=0
        print(s[i:j])
        while j<n+1:
            d=s[i:j]
            if len(set(d))==3:
                c+=1
            i+=1
            j+=1
        return c
