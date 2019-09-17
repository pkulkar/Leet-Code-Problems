class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashing={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashing:
                hashing[s[i]]+=1
            else:
                hashing[s[i]]=1
        for i in range(len(t)):
            if t[i] not in hashing:
                return False
            else:
                hashing[t[i]]-=1
        print(hashing)
        for num in hashing:
            if hashing[num]!=0:
                return False
        return True