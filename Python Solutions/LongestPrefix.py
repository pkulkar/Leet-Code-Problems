class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index=0
        strs.sort(key=len)
        answer=""
        if len(strs)==0:
            return ""
        while index<len(strs[0]):  
            letter=strs[0][index]
            count=0
            for j in range(len(strs)):
                if strs[j][index]!=letter:
                    return answer
                if strs[j][index]==letter:
                    count+=1
            if count==len(strs):
                answer+=letter
                    
            index+=1    
        return answer
            
            
        