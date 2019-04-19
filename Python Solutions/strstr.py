class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        else:
            for i in range(0,len(haystack)-len(needle)+1,1):
                sub=""
                for j in range(len(needle)):
                    sub+=haystack[i+j]                    
                if sub==needle:
                    return(i)
            return -1
        