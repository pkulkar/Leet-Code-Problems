class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(0,len(haystack)-len(needle)+1,1):
                sub=""
                for j in range(len(needle)):
                    sub+=haystack[i+j]                    
                if sub==needle:
                    return(i)
           
        