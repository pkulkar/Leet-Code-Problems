class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique=list()
        for email in emails:
            current=email
            count=0
            countat=0
            s=""
            for i in range(len(current)):
                if current[i]== '@':
                    countat+=1
                if current[i]=='+':
                    count+=1
                if countat>0:
                    s=s+current[i]
                else:
                    if count<1 and current[i]!='.':
                        s=s+current[i]
            if s not in unique:
                unique.append(s)
        return(len(unique))